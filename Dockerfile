FROM tensorflow/tensorflow:1.4.1

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-pip \
    python-opencv

RUN pip --no-cache-dir install \
    numpy \
    opencv-python \
    flask
    
ADD . /usr/src/app

WORKDIR /usr/src/app
EXPOSE 5000
CMD ["python", "server.py"]