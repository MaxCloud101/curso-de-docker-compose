FROM python:3.10.13

RUN apt-get update 

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV SERVER_ENV=development

EXPOSE 8000

CMD ["python3", "main.py" ]
