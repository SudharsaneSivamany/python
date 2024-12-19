FROM python:3.9-alpine

# Set environment variables
ENV PYTHONBUFFERED=1 REDISHOST=127.0.0.1 REDISPORT=6379

# Install system dependencies and Python packages
RUN apk update && \
    apk upgrade --no-cache

# Create non-root user
RUN addgroup -S nonroot && adduser -S appuser -G nonroot

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Adjust permissions and switch to non-root user
RUN chown -R appuser:nonroot /app
USER appuser

# Run the application
CMD ["python", "main.py"]