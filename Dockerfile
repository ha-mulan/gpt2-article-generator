FROM ham5312/fakenews:3.0


RUN git clone https://github.com/ha-mulan/gpt2-article-generator ham
RUN mv ham/app.py gpt2-article-generator/app.py
RUN mv ham/generator.py gpt2-article-generator/generator.py
RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils wget
        
RUN pip install --upgrade pip  
RUN pip install Flask gunicorn
RUN pip install flask && pip install waitress

WORKDIR /gpt2-article-generator/
EXPOSE 80
#COPY . . 
ENTRYPOINT ["python", "app.py"]
    
    
    
