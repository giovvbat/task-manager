# bringing python into container
FROM python:3.10-slim

# creating /app directory
WORKDIR /app

# copying requirements file and installing required dependencies
COPY docker/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copying code into container
COPY . /app/

# exposing django port
EXPOSE 8000

# commands to run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]