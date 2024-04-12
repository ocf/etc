FROM python:3.11-alpine
RUN apk add git rsync
COPY sync-etc .
ENTRYPOINT ["./sync-etc"]
