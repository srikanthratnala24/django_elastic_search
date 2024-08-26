# Use the official Python image as a base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Install dependencies from Pipfile
RUN pipenv install --deploy --system

# Copy the entire project
COPY . /app/

# RUN pipenv python manage.py makemigrations
# RUN pipenv python manage.py migrate
# RUN pipenv python manage.py search_index --rebuild

# Expose port 8000
EXPOSE 8000

# Run migrations and start the Django development server
# CMD ["pipenv", "run", "sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["sh", "-c", "pipenv run python manage.py makemigrations && pipenv run python manage.py migrate && pipenv run python manage.py search_index --rebuild && pipenv run python manage.py runserver 0.0.0.0:8000"]
