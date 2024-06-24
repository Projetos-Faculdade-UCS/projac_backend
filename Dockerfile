FROM python:alpine3.19

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Install system dependencies and Python dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && apk add --no-cache postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Copy the application code into the image
COPY ./app /app

# Expose the port the app runs on
EXPOSE 8000

# Set the command to run the application
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]