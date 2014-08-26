from samantha import celery


@celery.task
def greet(who):
    return 'Hello %s!' % who.capitalize()
