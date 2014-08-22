from redis import Redis

from samantha import app, config

redis = Redis(host=config.get('REDIS_HOST'), port=config.get('REDIS_PORT'))


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')
