# From python3.9 base image
FROM python:3.9

# Set current working directory
WORKDIR /MLCapstone

# Copy requirements file first to the working directory
COPY ./requirements.txt /MLCapstone/requirements.txt

# Install package dependencies
RUN pip install --no-cache-dir --upgrade -r /MLCapstone/requirements.txt

# copy files and directory to the working directory
COPY ./app /MLCapstone/app/
COPY ./data /MLCapstone/data/
COPY ./model /MLCapstone/model/
COPY ./static /MLCapstone/static/
COPY ./templates /MLCapstone/templates/

# run uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
