import json

redis_host = raw_input('[Redis Host]:')
redis_port = raw_input('[Redis Port No]:')
redis = 'redis://'+redis_host+':'+redis_port+'/0'
redis_queues = ['default', 'high', 'medium', 'low']
try:
    with open('config.json', 'r') as f:
        data = json.load(f)
except:
    data = {}

data['redis'] = {}
data['redis']['url'] = redis
data['redis']['host'] = redis_host
data['redis']['port'] = redis_port
data['redis']['queues'] = redis_queues

with open('config.json', 'w') as f:
    json.dump(data, f, indent=2)
