FROM ham5312/fakenewsgpu:1.1



RUN pip install waitress
COPY . .
RUN mv app.py modelInfo/app.py
RUN mv app2.py modelInfo/app2.py

RUN mv templates modelInfo/
WORKDIR /modelInfo/
EXPOSE 80

ENTRYPOINT ["python", "app2.py"]
    
    
    
