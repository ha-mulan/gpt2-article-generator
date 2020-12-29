FROM ham5312/fakenews:2.0




RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils wget
        
RUN pip install --upgrade pip  
RUN pip install Flask gunicorn
RUN pip install flask && pip install waitress
RUN mkdir gpt2-article-generator
COPY . /gpt2-article-generator
RUN mv ham/checkpoint gpt2-article-generator/checkpoint
RUN mv ham/models gpt2-article-generator/models
WORKDIR /gpt2-article-generator/
EXPOSE 80

ENTRYPOINT ["python", "app.py"]
    
    
    
