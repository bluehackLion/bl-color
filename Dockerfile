FROM bluelens/tensorflow:latest-gpu-py3

RUN mkdir -p /usr/src/app/model

WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/grpc

CMD ["python", "feature_extract_server.py"]
