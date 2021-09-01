FROM python:3.9.6

WORKDIR /app

COPY requirements.txt ./requirements.txt


RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y libsndfile1-dev

EXPOSE 8080

COPY . /app


CMD streamlit run --server.port 8080 --server.enableCORS false app.py
