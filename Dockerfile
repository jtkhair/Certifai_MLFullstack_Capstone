FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY ./model/mlp_pwr_best_model /model/
COPY ./app /app