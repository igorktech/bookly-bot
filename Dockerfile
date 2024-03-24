FROM python:3.10-slim-buster

LABEL authors="igorktech"

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the command to start your bot
CMD ["python", "__main__.py"]