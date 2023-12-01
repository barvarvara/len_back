FROM python:3.12-alpine3.17

# set environment variables
ENV DockerHOME=/len_back
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $DockerHOME

COPY requirements.txt $DockerHOME/requirements.txt

RUN pip install -r $DockerHOME/requirements.txt

COPY . $DockerHOME

# start server
#CMD python manage.py runserver 0.0.0.0:8000