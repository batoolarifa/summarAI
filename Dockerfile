# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    APP_HOME=/app

# Set working directory
WORKDIR $APP_HOME

# Copy app files
COPY app/ ./app/
COPY summary_model/ ./summary_model/
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Start the app
CMD ["flask", "run"]