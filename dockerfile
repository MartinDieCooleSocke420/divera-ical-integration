# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose the desired port
EXPOSE 1312

# Run Gunicorn exposing at 1312
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:1312", "main:app"]
