FROM ubuntu:latest
LABEL authors="a.sedov"

ENTRYPOINT ["top", "-b"]