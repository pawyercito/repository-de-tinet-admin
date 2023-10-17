#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
FROM python:3.9-alpine

# Create function directory
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app

EXPOSE 80
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "80"]
