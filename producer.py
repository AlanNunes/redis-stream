import redis
import random
import asyncio
from redis.exceptions import ResponseError

stream_key = 'driver_geolocation'

async def send_geolocation(redisCli):
    lat = random.random()
    long = random.random()
    redisCli.xadd(name=stream_key, fields={"longitude": long, "latitude": lat})

async def main():
    group = 'route_calculator'
    redisCli = redis.Redis(host='127.0.0.1', port=6005)

    try:
        redisCli.xgroup_create( name=stream_key, groupname=group, id=0 )
        print("The consumer group was created successfully")
    except ResponseError as e:
        print("The consumer group already exists.")

    batch_size = 500
    batch_count = 1
    while True:
        tasks = [send_geolocation(redisCli) for _ in range(0, batch_size)]
        await asyncio.gather(*tasks)
        print(f"Batch {batch_count} enviado com tamanho {batch_size}.")
        batch_count += 1

if __name__ == "__main__":
    asyncio.run(main())