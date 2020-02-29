FROM python:3.7

RUN pip install gunicorn

COPY docker/settings.ini /app/cb_news/news_extractor/settings.ini

COPY . /app

RUN pip install -r /app/requirements.txt
RUN pip install /app/

ARG FB_TOKEN_ARG
ENV FB_TOKEN=$FB_TOKEN_ARG

WORKDIR /app/cb_news/news_extractor
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]


