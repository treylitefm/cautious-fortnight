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

def fetch_audio(url, file_name=None):
    db = Model()
    
    if db.has_already_been_downloaded(url):
        print 'Skipping,', url, 'has already been downloaded'
        return False

    db.insert_dl_url(url)
    
    #import time; time.sleep(5) #simulates the download time
    __download(url)

    db.update_dl_url_to_finished(url)
