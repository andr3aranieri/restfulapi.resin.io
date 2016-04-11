#Set the base os
FROM resin/raspberrypi-python

# File Author / Maintainer
MAINTAINER Andrea Ranieri

# Enable systemd
ENV INITSYSTEM on

# Install Python.
RUN apt-get update \
	&& apt-get install -y python python-pip python-dev build-essential libffi-dev libssl-dev \
	# Remove package lists to free up space
	&& rm -rf /var/lib/apt/lists/*

# Copy current directory into /app
COPY . /app

RUN pip install --upgrade pip

RUN  pip install pyopenssl ndg-httpsclient pyasn1

# Install python dependencies from requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# create data store edit scripts
CMD ["python", "/app/manage.py", "makemigrations", "restfulapi"]

# execute sql scripts to make changes on data store
CMD ["python", "/app/manage.py", "migrate"]

# run python script when container lands on device
CMD ["python", "/app/manage.py", "runserver 0.0.0.0:80"]
