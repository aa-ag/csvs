FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /spa
WORKDIR /spa
COPY . .
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 8080/tcp