from flask import Flask

from samantha import config

# configure Flask
app = Flask(__name__)

# configure SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

# configure Redis
from redis import Redis
redis = Redis(host=config.get('REDIS_HOST'), port=config.get('REDIS_PORT'))

# configure Celery
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

app.config.update(
    CELERY_BROKER_URL=config.get('CELERY_BROKER_URL'),
    CELERY_RESULT_BACKEND=config.get('CELERY_BROKER_URL'),
    CELERY_ACCEPT_CONTENT=[config.get('CELERY_ACCEPT_CONTENT'), 'pickle']
)
celery = make_celery(app)
