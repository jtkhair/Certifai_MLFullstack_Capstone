"""
Web server script that exposes endpoints and pushes ship principal parameter data (csv file) to Redis for passenger
ship powering by model server. Polls Redis for response from model server.

Deployment is based on pretrained model developed using scikit learn
"""

# %%
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from io import StringIO
import codecs
import csv
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from io import StringIO
import json
import logging
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from typing import Optional
import matplotlib.pyplot as plt

scaler = MinMaxScaler()

# %%

# app configuration
app = FastAPI(title="Passenger Ship Powering Prediction",
              description="API for passenger ship powering prediction using Deep Learning")

# css folder
app.mount(
    "/static",
    StaticFiles(directory="../static"),
    name="static")

# mount jinja template
templates = Jinja2Templates(directory="../templates")

# Log setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")

# load model/scaler
model = pickle.load(open("../model/mlp_pwr_best_model.sav", 'rb'))
scaler = pickle.load(open("../model/scaler_pwr.sav", 'rb'))


# home page
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

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
        df = pd.read_csv(prep_data)

        # html table
        table = df.to_html(justify="center", index=None, classes=["table", "table-hover"])

        # sample graph
        graph_data = df[['Vs','P']].values.tolist()
        graph_data.insert(0,["Vs", "P"])
        
        '''
        all your processes will be here :)
        '''

        return templates.TemplateResponse("home_copy.html", {"request": request, "table": table, "graph_data": graph_data})


# @app.post("/predict")
# async def get_prediction():

# # preprocessing
# dataset_scaled = scaler.fit_transform(df)
# df_scaled = pd.DataFrame(dataset_scaled, index=df.index)
# df_scaled.columns = ['LWL', 'B', 'T', 'L/B', 'B/T', 'Disp', 'CB', 'Vs', 'Fn', 'P']

# X = df_scaled.drop(['P'], 1)
# y = df_scaled['P']

#     prediction_mlp = model.predict(X)

# print('MultiLayer Perceptron Regression (Train-80%, Test-20%)\n')
# print('MAE:', metrics.mean_absolute_error(y, prediction_mlp))
# print('MSE:', metrics.mean_squared_error(y, prediction_mlp))
# print('RMSE:', np.sqrt(metrics.mean_squared_error(y, prediction_mlp)))
# print('Test score:', model.score(X, y))

# save to file
# df_output.to_csv("data/output.csv", index=False)

# return()

# %%

# # Load data
# df = pd.read_csv("../../Data/MonoROPAX_Training.csv").drop(['ID', 'D', 'Npax', 'Nveh', 'GT'], 1)
#
