from flask import Flask, Response, request, json
from youtube_dl import fetch_audio
from ast import literal_eval

app = Flask(__name__)

@app.route('/')
def index():
    return json.jsonify({})

@app.route('/download', methods=['POST'])
def download():
    data = literal_eval(request.data)

    if 'url' not in data:
        raise Exception

    download_url = data['url']

    if not __valid_youtube_url(download_url):
        raise Exception
    
    fetch_audio(download_url)

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
    # app.debug = True
    app.run(host='0.0.0.0')
