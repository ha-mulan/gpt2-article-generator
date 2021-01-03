FROM ham5312/fakenewsgpu:1.1



RUN pip install waitress
COPY . .
RUN mv app.py modelInfo/app.py
RUN mv templates modelInfo/
WORKDIR /modelInfo/
EXPOSE 80

ENTRYPOINT ["python", "app.py"]
    
    
    
