# Backend + frontend served by Flask
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src
COPY public /app/public

ENV FLASK_APP=src/app.py
ENV PORT=4000

EXPOSE 4000
CMD ["python", "-m", "src.app"]
