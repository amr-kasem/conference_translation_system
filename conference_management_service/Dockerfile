# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to avoid Python buffering and set working directory
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Set the default command to run the FastAPI app using Uvicorn
CMD ["python3", "main.py", "--api-host", "0.0.0.0", "--api-port", "8000","--messaging-host", "nats", "--messaging-port", "4222", "start"]
# python3 main.py --api-host 0.0.0.0 --api-port 8000 --messaging-host nats --messaging-port 4222 start