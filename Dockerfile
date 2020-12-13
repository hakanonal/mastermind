FROM python:3.7.2

COPY / /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT 5000

# 5
CMD exec python api.py