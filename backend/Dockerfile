# Dockerfile for local dev server
FROM python:3.8

WORKDIR /app

COPY ./app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
