# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the FLASK_APP environment variable and expose port 5000
ENV FLASK_APP=app.py
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
