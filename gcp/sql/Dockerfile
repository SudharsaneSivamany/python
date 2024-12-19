# Use an official Python runtime as the base image
FROM python:3.9-alpine

ENV PYTHONBUFFERED=1 DB_USER=your_db_user DB_PASS=your_db_password DB_NAME=your_db_name

RUN apk update && \
    apk upgrade --no-cache

# Create non-root user
RUN addgroup -S nonroot && adduser -S appuser -G nonroot

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir psycopg2-binary==2.9.10

# Adjust permissions and switch to non-root user
RUN chown -R appuser:nonroot /app
USER appuser

# Run the Python script
CMD ["python", "main.py"]