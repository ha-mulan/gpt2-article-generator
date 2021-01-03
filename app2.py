import os
import io
from flask import Flask, render_template, request, Response, send_file, jsonify
from queue import Queue, Empty
from generator import *
from ArticleGenerator import *
import threading
import time
from flask import Flask
from flask import request
from primeFactor import PrimeFactor
app = Flask(__name__)

requests_queue = Queue()
BATCH_SIZE = 1
CHECK_INTERVAL = 0.1

# static variable

# request handling
def handle_requests_by_batch():
    Generatored=Generator.get_instance()
    try:
        while True:
            requests_batch = []
            while not (len(requests_batch) >= BATCH_SIZE):
                try:
                    requests_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
                except Empty:
                    continue

            batch_outputs = []

            for request in requests_batch:
                if len(request["input"]) == 1:
                    list_news=Generatored.generate(initial_content=request['input'][1],title=request['input'][0])
                    listToStr = ' '.join(map(str,list_news))
                    batch_outputs.append(listToStr)
            for request, output in zip(requests_batch, batch_outputs):
                request["output"] = output

    except Exception as e:
        while not requests_queue.empty():
            requests_queue.get()
        print(e)

threading.Thread(target=handle_requests_by_batch).start()

@app.route("/api/", methods=['GET'])
def generate():

    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'error': 'Too Many Requests'}), 429

    try:
        args = []

        titled=request.args.get('title')
        contented=request.args.get('content')

        args.append((titled,contented))

    except Exception:
        print("Empty Text")
        return Response("fail", status=400)

    req = {
        'input': args
    }
    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    return req['output']


@app.route('/healthz')
def health():
    return "ok", 200

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
