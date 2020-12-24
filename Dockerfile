from ham5312/fakenews:3.0

RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils wget

RUN pip install --upgrade pip
RUN pip install transformers \
    tensorboard \
    wandb
    
RUN pip install Flask gunicorn
RUN pip install flask && pip install waitress

WORKDIR /gpt2-article-generator/
EXPOSE 8000
COPY . .
ENTRYPOINT ["python", "app.py"]



