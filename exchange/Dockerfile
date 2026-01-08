FROM python:3.10.13

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "main.py" ]
