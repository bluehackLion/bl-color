FROM bluelens/tensorflow:latest-gpu-py3

RUN mkdir -p /opt/app/model

WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/grpc

RUN curl https://s3.ap-northeast-2.amazonaws.com/bluelens-style-model/classification/color/dev/color_classification_model.pb  -o /opt/app/model/classify_image_graph_def.pb
RUN curl https://s3.ap-northeast-2.amazonaws.com/bluelens-style-model/classification/color/dev/labels.txt  -o /opt/app/model/labels.txt
ENV CLASSIFY_GRAPH=/Users/lion/PycharmProjects/bl-color/color_classification_model.pb
ENV LABEL_MAP=/Users/lion/PycharmProjects/bl-color/labels.txt

CMD ["python", "color_extract_server.py"]
