FROM python:3.8
MAINTAINER Alban Maxhuni, PhD <almax@dtu.dk>

# Set the working directory to /ipdmgo
WORKDIR /carp_flask

# Copy the current directory contents into the container at /ipdmgo
ADD . /carp_flask

# Install the dependencies
COPY ./requirements.txt /carp_flask/requirements.txt
RUN pip3 install -r requirements.txt

# Uwsgi
RUN pip3 install uwsgi
RUN pip3 install uwsgi-tools
RUN pip3 install carp-python-api==1.0.6

RUN apt-get update

COPY . /carp_flask

EXPOSE 8091

### Run the command to start uWSGI
CMD ["uwsgi", "--ini", "app.ini"]
