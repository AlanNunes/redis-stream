import redis

redisCli = redis.Redis(host='127.0.0.1', port=6379)

stream_key = 'driver_geolocation'
group = 'route_calculator'

try:
    redisCli.xgroup_create( name=stream_key, groupname=group, id=0 )
except:
    print("Consumer already exists")

while True:
    resp = redisCli.xreadgroup( groupname=group, consumername='c', block=500, streams={stream_key:'>'}, count=500)
    if not resp:
        print('Waiting data to consume')
        continue
    for key, value in resp[0][1]:
        item = {'latitude': value[b'latitude'].decode(), 'longitudade': value[b'longitude'].decode()}
        print(f'Rota calculada para localização: {item}')