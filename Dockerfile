FROM python:3.7.2

COPY / /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

RUN useradd -m myuser
USER myuser

CMD exec python api.py