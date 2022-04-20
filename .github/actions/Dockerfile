FROM python:3.9.5-slim

RUN apt update; \
    apt install -y git
RUN pip install "pysen[lint]" click==8.0.4

ENTRYPOINT ["pysen", "run", "lint"]