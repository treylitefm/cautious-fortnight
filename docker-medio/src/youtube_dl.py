import json
import os
from model import Model

def __download(url):
    directory = 'music'
    if not os.path.exists(directory): 
        print 'Warning! Directory',directory,'does not exist -- Creating it now'
        os.makedirs(directory)

    bashCommand = "youtube-dl \""+url+"\" --audio-format mp3 --extract-audio -o \""+directory+"/"+"%(title)s-%(id)s.%(ext)s\""
    os.system(bashCommand)

def fetch_audio(url, file_name=None, db=None):
    if not db:
        db = Model()
    
    url = normalize_url(url)

    if db.has_already_been_downloaded(url):
        print 'Skipping,', url, 'has already been downloaded'
        return False

    db.insert_dl_url(url)
    
    #import time; time.sleep(5) #simulates the download time
    __download(url)

    db.update_dl_url_to_finished(url)

def normalize_url(url):
    '''Removes part of url that makes it a playlist so that worker only downloads single song'''
    amp = url.find('&')
    channel = url.find('ab_channel')
    if channel > 0 and amp > 0:
        return url[:amp+1]+url[channel:]
    elif amp > 0:
        return url[:amp]
    else:
        return url
