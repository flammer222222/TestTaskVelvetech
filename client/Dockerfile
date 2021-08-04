FROM python:3.8 AS builder
COPY requirements.txt .


RUN pip3 install --user -r requirements.txt

FROM python:3.8.10-slim
WORKDIR ./

COPY --from=builder /root/.local /root/.local
COPY ./client.py /

ENV PATH=/root/.local:$PATH


CMD ["python3", "-u","./client.py"]




