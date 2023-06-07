from python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "5000", "app:app"]
