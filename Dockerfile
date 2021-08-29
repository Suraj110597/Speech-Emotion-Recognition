FROM python:3.9.6

WORKDIR /app

COPY requirements.txt .

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \ libsndfile1 
EXPOSE 8080

COPY . /appz

CMD streamlit run --server.port 8080 --server.enableCORS false app.py
