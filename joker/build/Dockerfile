FROM python:3.9-slim
WORKDIR /app
COPY /python/requirements.txt .
RUN pip install -r requirements.txt
COPY /python/app.py .
CMD ["python", "app.py"]

