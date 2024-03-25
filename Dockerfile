FROM python:3.10-slim-buster

LABEL authors="igorktech"

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
#EXPOSE $PORT

CMD ["python", "__main__.py"]