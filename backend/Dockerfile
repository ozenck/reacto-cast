# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Run the command to start uWSGI
# CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "reacto_cast.wsgi:application", "--processes", "1", "--threads", "8"]
# uvicorn reacto_cast.asgi:application --host 0.0.0.0 --port 8000 --reload