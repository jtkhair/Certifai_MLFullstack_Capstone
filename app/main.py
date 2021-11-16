"""
>
>**Copyright &copy; 2021 Jauhari Khairuddin**<br>
>
>This program is a free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or any later version.
>
>This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
>
>    You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.<br>
>
Web application that accept ship principal parameter data (csv file) to perform prediction for passenger
ship powering
>
Deployment is based on pretrained model developed using scikit learn library
"""

from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from io import StringIO
import logging
import pandas as pd
import pickle

# app configuration
app = FastAPI(title="Passenger Ship Powering Prediction",
              description="API for passenger ship powering prediction using Deep Learning")

# css folder
app.mount(
    "/static",
    StaticFiles(directory="./static"),
    name="static")

# mount jinja template
templates = Jinja2Templates(directory="./templates")

# Log setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")

# load model & scaler
model = pickle.load(open("./model/mlp_pwr_base3_best_model.sav", 'rb'))
scaler = pickle.load(open("./model/scaler_pwr.sav", 'rb'))

# home page
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# page2
@app.post("/uploadfile/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    # only accept csv
    if file.filename.split(".")[-1] != "csv":
        return {"error": "undefined file extension"}
    else:
        # return byte
        raw_data = await file.read()

        # byte to str
        str_data = str(raw_data,'utf-8')

        # prepare string as input for pandas
        prep_data = StringIO(str_data)

        # create df
        df = pd.read_csv(prep_data).round(2)

        # html table
        input_table = df.values.tolist()
        input_header = df.columns

        # Preprocess data
        data_scaled = scaler.transform(df.drop(['D', 'GT'], 1))
        df_data_scaled = pd.DataFrame(data_scaled, index=df.index)
        df_data_scaled.columns = ['LWL', 'B', 'T', 'L/B', 'B/T', 'Disp', 'CB', 'Vs', 'Fn', 'P']

        #  Create label
        X = df_data_scaled.drop(['P'], 1)

        # Infer powering
        predict_P = model.predict(X)

        # merge predicted_P to df
        df_predict_P = X
        df_predict_P['P'] = predict_P.tolist()

        # inverse scale
        predicted_P = scaler.inverse_transform(df_predict_P)
        df_predicted_P = pd.DataFrame(predicted_P, index=X.index)
        df_predicted_P.columns = ['LWL', 'B', 'T', 'L/B', 'B/T', 'Disp', 'CB', 'Vs', 'Fn', 'P']

        # merge scaled P to input file
        df['P'] = df_predicted_P['P']
        df_output = df.round(2)

        # Output table
        output_table = df_output.values.tolist()
        output_header = df.columns

        # save to file
        df_output.to_csv("./data/output.csv", index=False)

        # sample graph
        graph_data = df_output[['Vs', 'P']].values.tolist()
        graph_data.insert(0, ['Vs', 'Predicted P'])

        return templates.TemplateResponse("Page2.html",
            {
                "request": request,
                "input_table": input_table,
                "input_header": input_header,
                "output_table": output_table,
                "output_header": output_header,
                "graph_data": graph_data
            })
