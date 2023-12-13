FROM python:3.11-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# deploy flask to cloud run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
