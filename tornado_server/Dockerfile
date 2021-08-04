FROM python:3.8 AS builder
COPY requirements.txt .


RUN pip3 install --user -r requirements.txt

FROM python:3.8.10-slim
WORKDIR ./

COPY --from=builder /root/.local /root/.local
COPY ./tornado_server.py /
COPY ./filter ./filter

ENV PATH=/root/.local:$PATH

CMD ["python3", "-u", "./tornado_server.py"]



