FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app ./app
COPY gen ./gen
COPY proto ./proto
COPY .env ./
COPY main.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]

EXPOSE 5000