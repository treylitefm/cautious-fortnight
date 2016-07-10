import json
import sys

if len(sys.argv) is not 3:
    print 'Pass in host and port, likes so:'
    print 'python configure.py 123:123:123:213 6379'
    print '--- or ---'
    print 'python configure.py example.com 7833'
    sys.exit(1)

redis_host = sys.argv[1]
redis_port = sys.argv[2]

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
