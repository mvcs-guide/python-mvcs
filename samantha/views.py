from samantha import app, redis
from samantha.tasks import square


@app.route('/')
def hello():

    # do some work in redis
    redis.incr('hits')
    hits = redis.get('hits')

    # do some work in celery
    result = square.delay(hits)
    result.wait()
    result = result.get()

    return 'Hello World! I have been seen %s times. %s squared is %d' % (hits, hits, result)
