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

    data['downloads'][url] = {
        'start': True,
        'complete': False if not done else True
    }

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

def download(url, file_name=None):
    if file_name is None:
        file_name = 'data.json'

    __save_url(file_name, url)
    import time; time.sleep(5)
    __save_url(file_name, url, True)
