FROM ham5312/fakenewsgpu:1.1




#RUN apt-get update && \
#    apt-get install -y && \
#    apt-get install -y apt-utils wget
        
#RUN pip install --upgrade pip  
#RUN pip install Flask gunicorn
#RUN pip install flask && pip install waitress
#RUN mkdir gpt2-article-generator
#COPY . /gpt2-article-generator
#RUN mv ham/checkpoint gpt2-article-generator/checkpoint
#RUN rm -rf gpt2-article-generator/models
#RUN mv ham/models gpt2-article-generator
#WORKDIR /gpt2-article-generator
#RUN mkdir gpt2-article-generator
COPY . .
RUN mv gpt2-article-generator/app.py modelInfo/app.py
WORKDIR /modelInfo/
EXPOSE 80

ENTRYPOINT ["python", "app.py"]
    
    
    
