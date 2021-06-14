FROM python:3.9
ENV PYTHONDUFFERED=1
WORKDIR . ./
COPY requirements.txt . ./
RUN pip3 install -r requirements.txt
COPY . ./