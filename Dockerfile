FROM amazonlinux:latest

ENV TZ=Asia/Hong_Kong
RUN sleep 3

CMD ["sleep", "4"]