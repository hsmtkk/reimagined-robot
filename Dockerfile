FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
