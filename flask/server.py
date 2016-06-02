from flask import Flask, Response, request, json
from youtube_dl import fetch_audio
from ast import literal_eval

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/download', methods=['POST'])
def download():
    print request.data

    data = literal_eval(request.data)

    if 'url' not in data:
        raise Exception

    download_url = data['url']

    if not __valid_url(download_url):
        raise Exception
    
    #import ipdb; ipdb.set_trace()
    fetch_audio(download_url)

    return json.jsonify({
        'success': True,
        'download_url': download_url
    })


def __valid_url(url):
    '''
    Validate that data passed is actually an url and
    enumerate acceptable download domains
    '''

    #soundcloud and youtube
    return True

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
