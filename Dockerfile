FROM python:3.12-alpine3.17

# set environment variables
ENV DockerHOME=/len_back
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# where your code lives
WORKDIR $DockerHOME

# run this command to install all dependencies
COPY requirements.txt $DockerHOME/requirements.txt

#    && apk install -y postgresql postgresql-contrib libpq-dev python3-dev \
RUN pip install -r $DockerHOME/requirements.txt
#    adduser --disabled-password len_back-user

# Clear cache
# RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# USER len_back-user

# port where the Django app runs
#EXPOSE 8000

# copy whole project to your docker home directory.
COPY . $DockerHOME

# start server
#CMD python manage.py runserver 0.0.0.0:8000