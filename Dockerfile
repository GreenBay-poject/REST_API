# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /REST_API

# Set the working directory to /REST_API
WORKDIR /REST_API

# Copy the current directory contents into the container at /REST_API
ADD . /REST_API/

# Install any needed packages specified in requirements.txt
RUN pip uninstall earthengine-api
RUN pip uninstall ee
RUN pip install -r requirments.txt

