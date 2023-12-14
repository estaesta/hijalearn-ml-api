FROM python:3.11.7-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

# deploy flask to cloud run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
