FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
EXPOSE 3000

CMD [ "uvicorn", "djangoapp.asgi:application", "--workers","1", "--host", "0.0.0.0","--port", "3000" ]
