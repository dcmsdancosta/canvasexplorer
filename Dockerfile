FROM python:3.7-slim

RUN apt-get update && apt-get install -y libgomp1

WORKDIR ./src

COPY ./src ./

RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py