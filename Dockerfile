FROM python:3.5-slim
MAINTAINER JS Tan "jianshentan@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5002 80 
ENTRYPOINT ["python"]
CMD ["application.py"]
