# from generator import *
# from ArticleGenerator import *
# import os
# from subprocess import check_output
# from flask import Flask
# from flask import request
# app = Flask(__name__)

# @app.route('/')
# def homepage():
#     # target = os.environ.get('TARGET', 'World')
#     # try:
#     # keyword=request.args.get('keyword')

#     #stream = os.popen(f'python3 ArticleGenerator.py {keyword} -C {keyword} -p')
#     # return check_output('ls -al')
#     return 'to generate article please add /api/title/content at the end of url'


# @app.route('/api/')
# def api():
#     titled=request.args.get('title')
#     contented=request.args.get('content')

#     Generatored=Generator.get_instance()
#     # return titled+contented
#     list_news=Generatored.generate(initial_content=contented,title=titled)
#     listToStr = ' '.join(map(str,list_news))
#     return listToStr
#     # return title+content
#         # return check_output(f'python3 ArticleGenerator.py {keyword} -C {keyword} -p')
#     # except:
#         # return 'NO KEYWORD!!! please give the input by adding  <  ?keyword={your keyword} > at the end of url'

# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0',threaded=False,port=int(os.environ.get('PORT', 80)))
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
    list_news=Generatored.generate(title=value1,content=value2)
    listToStr = ' '.join(map(str,list_news))
    return listToStr
@app.route('/api/<title>/<content>')
def api(title,content):
    try:
        Generatored=Generator.get_instance()
        list_news=Generatored.generate(title=title,content=content)
        listToStr = ' '.join(map(str,list_news))
        return listToStr
    except:
        return 'to generate article please add /api/title/content at the end of url'
    # return title+content
        # return check_output(f'python3 ArticleGenerator.py {keyword} -C {keyword} -p')
    # except:
        # return 'NO KEYWORD!!! please give the input by adding  <  ?keyword={your keyword} > at the end of url'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8000)))
