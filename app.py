import os
from subprocess import check_output
from flask import Flask
from flask import request
from generator import *
from ArticleGenerator import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    #try:
    target = os.environ.get('TARGET', 'World')
    keyword=request.args.get('keyword')
    list_news=Generator.generate(keyword,title=keyword)
    listToStr = ' '.join(map(str,list_news))
    return listToStr
    #except:
     #   return 'NO KEYWORD!!! please give the input by adding  <  ?keyword={your keyword} > at the end of url'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',threaded=False,port=int(os.environ.get('PORT', 80)))

# host.docker.internal
