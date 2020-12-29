from generator import *
from ArticleGenerator import *
import os
from subprocess import check_output
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def homepage():
    # target = os.environ.get('TARGET', 'World')
    # try:
    # keyword=request.args.get('keyword')

    #stream = os.popen(f'python3 ArticleGenerator.py {keyword} -C {keyword} -p')
    # return check_output('ls -al')
    return 'to generate article please add /api/title/content at the end of url'


@app.route('/api/')
def api():
    titled=request.args.get('title')
    contented=request.args.get('content')

#     Generatored=Generator()
    # return titled+contented
    list_news=Generator.generate(initial_content=contented,title=titled)
    listToStr = ' '.join(map(str,list_news))
    return listToStr
    # return title+content
        # return check_output(f'python3 ArticleGenerator.py {keyword} -C {keyword} -p')
    # except:
        # return 'NO KEYWORD!!! please give the input by adding  <  ?keyword={your keyword} > at the end of url'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',threaded=False,port=int(os.environ.get('PORT', 80)))
