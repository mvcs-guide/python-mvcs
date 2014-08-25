from samantha import celery


@celery.task
def square(num):
    return int(num) * int(num)