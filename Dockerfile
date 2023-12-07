FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y tesseract-ocr

RUN pip install gunicorn

RUN pip install -r requirements.txt

ENV PORT=4000
EXPOSE 4000
 
CMD ["gunicorn", "-b", "0.0.0.0:4000", "src.api:app"]