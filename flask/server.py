from flask import Flask, Response, request, json
from flask_cors import cross_origin
from youtube_dl import fetch_audio
from ast import literal_eval
from queue import MedioQueue
import re

app = Flask(__name__)
q = MedioQueue()

@app.route('/')
def index():
    return 'Sup World!'

@app.route('/download', methods=['POST', 'OPTIONS'])
@cross_origin()
def download():
    data = literal_eval(request.data)

    if 'url' not in data:
        return json.jsonify({
            'success': False,
            'reason': 'url not in request'
        })

    download_url = data['url']

    if not __valid_youtube_url(download_url):
        return json.jsonify({
            'success': False,
            'reason': 'invalid url'
        })
    
    q.process(fetch_audio, download_url)

    return json.jsonify({
        'success': True,
        'download_url': download_url
    })


def __valid_youtube_url(url):
    '''
    Filter out non-youtube urls
    '''
    match = re.match('https:\/\/.+youtube\..+', url)
    if match is None:
        return False

    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0')
