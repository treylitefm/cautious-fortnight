import json

with open('config.json', 'r') as f:
    config = json.load(f)

REDIS_URL = config['redis']['url']

QUEUES = config['redis']['queues']


print REDIS_URL, QUEUES
