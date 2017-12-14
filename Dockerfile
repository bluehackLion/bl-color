FROM bluelens/tensorflow:latest-gpu-py3

RUN mkdir -p /opt/app/model

WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/grpc

RUN curl https://s3.ap-northeast-2.amazonaws.com/bluelens-style-model/classification/inception_v3/classify_image_graph_def.pb -o /opt/app/model/classify_image_graph_def.pb
ENV CLASSIFY_GRAPH=/opt/app/model/classify_image_graph_def.pb

CMD ["python", "feature_extract_server.py"]
