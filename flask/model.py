from redis import Redis
import json
import os, time

class Model:
    '''Handle redis schema and CRUD'''
    config = None
    conn = None

    def __init__(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)

        self.conn = Redis(self.config['redis']['host']) 
        os.environ['TZ'] = 'EST'
        time.tzset()

    def get_dl_url(self, url):
        return self.conn.hgetall('downloads:'+url)

    def has_already_been_downloaded(self, url):
        result = self.get_dl_url(url)

        if bool(result) is not False and bool(result['finished']) is True:
            return True
        return False

    def insert_dl_url(self, url):
        return self.conn.hmset('downloads:'+url, {'started': True, 'finished': False, 'created_on': self.get_time(), 'updated_on': self.get_time()})

    def update_dl_url_to_finished(self, url):
        return self.conn.hmset('downloads:'+url, {'finished':True, 'updated_on': self.get_time()})

    def get_time(self):
        return time.strftime('%x %X %Z')
