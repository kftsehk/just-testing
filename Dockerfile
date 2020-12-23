FROM amazonlinux:latest

ENV TZ=Asia/Hong_Kong
RUN sleep 2

CMD ["sleep", "4"]