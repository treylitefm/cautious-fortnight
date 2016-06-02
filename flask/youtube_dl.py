import json

def __load(file_name):
    with open(file_name) as data:
        data = json.load(data)

    return data

def __save_url(file_name, url, done=False):
    try:
        data = __load(file_name)
    except Exception as e:
        print 'Warning!', file_name, 'does not exist. So I\'m creating it now'
        data = {'downloads':{}}

    if url in data['downloads']:
        if data['downloads'][url]['complete'] is True:
            print 'Skipping,', url, 'has already been downloaded'
            return False

    data['downloads'][url] = {
        'start': True,
        'complete': False if not done else True
    }

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

    return True

def __download(url):
    bashCommand = "youtube-dl \""+url+"\" --audio-format mp3 --extract-audio -o \"%(title)s-%(id)s.%(ext)s\""
    import os; os.system(bashCommand)

def fetch_audio(url, file_name=None):
    if file_name is None:
        file_name = 'data.json'

    if not __save_url(file_name, url):
        return
    #import time; time.sleep(5) #simulates the download time
    __download(url)
    __save_url(file_name, url, True)
