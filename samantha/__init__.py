from flask import Flask

from samantha import config

# configure Flask
app = Flask(__name__)


# configure SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    config.get('SQLALCHEMY_DATABASE_URI'), 
    convert_unicode=True
)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


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
    CELERY_ACCEPT_CONTENT=config.get('CELERY_ACCEPT_CONTENT').split(',')
)
celery = make_celery(app)
