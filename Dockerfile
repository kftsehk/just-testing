FROM amazonlinux:latest

ENV TZ=Asia/Hong_Kong
RUN yum install python3 -y
ADD ./app.py .

CMD ["python3", "app.py"]