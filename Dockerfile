FROM nvidia/cuda:10.2-cudnn8-runtime-ubuntu16.04
COPY . /foldername

RUN apt-key del 7fa2af80 \ 
    && apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/3bf863cc.pub \ 
    && apt-get update

RUN apt-get install -y software-properties-common 
    

RUN add-apt-repository -y ppa:jblgf0/python \
&& apt-get update

RUN apt install wget

# RUN dpkg -i ./cuda-keyring_1.0-1_all.deb

RUN apt-get install -y python-distutils-extra

RUN apt-get install -y python3.8 python3-pip python3.8-dev python3.8-distutils

RUN wget  https://bootstrap.pypa.io/get-pip.py  --no-check-certificate

RUN python3.8 get-pip.py

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /foldername
RUN pip3.8 install --upgrade pip 
RUN pip3.8 install -r requirement.txt 
RUN pip3.8 install Cython
RUN pip3.8 install numpy
RUN pip3.8 install -U insightface
RUN pip3.8 install djangorestframework
RUN pip3.8 install -U drf-yasg
RUN pip3.8 install onnxruntime-gpu==1.6.0
RUN pip3.8 install mxnet

RUN insightface-cli model.download buffalo_l

# CMD ["python3","./test.py"]
EXPOSE 5000
CMD ["python3.8", "./app/manage.py", "runserver", "0.0.0.0:5000"]