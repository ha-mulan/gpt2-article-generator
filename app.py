from generator import *
from ArticleGenerator import *
import os
from subprocess import check_output
from flask import Flask
from flask import request
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def test():
    return render_template('index.html')
@app.route('/post', methods=['POST'])
def post():
    Generatored=Generator.get_instance()
    value1 = request.form['title']
    value2 = request.form['content']
    list_news=Generatored.generate(initial_content=value2,title=value1)
    listToStr = ' '.join(map(str,list_news))
    return render_template('result.html',value=listToStr)
@app.route('/api/')
def api():
    titled=request.args.get('title')
    contented=request.args.get('content')
    Generatored=Generator.get_instance()
    list_news=Generatored.generate(initial_content=contented,title=titled)
    listToStr = ' '.join(map(str,list_news))
    return listToStr
if __name__ == "__main__":
     app.run(debug=True,host='0.0.0.0',threaded=False,port=int(os.environ.get('PORT', 80)))
