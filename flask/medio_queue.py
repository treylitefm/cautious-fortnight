from rq import Queue
from redis import Redis
import json

class MedioQueue:
    redis_conn = None
    q = None
    config = None

    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)

        self.redis_conn = Redis(self.config['redis']['host'], self.config['redis']['port'])
        self.q = Queue(connection=self.redis_conn)


    def process(self, f, *args, **kwargs):
        job = self.q.enqueue(f, *args, **kwargs)
        return job

