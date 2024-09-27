# redis-stream
A sample real time stream of a driver geolocation that is being collected, for route calculation.

# setup
``docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest``

# how to use
Run producer.py and then consumer.py to start streaming.