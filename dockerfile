# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app.py

# Copy and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application into the container
# This copies app.py AND the entire /templates folder
COPY . .

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]