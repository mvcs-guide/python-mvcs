from flask import Flask

from samantha import config

# configure flask
app = Flask(__name__)

# configure SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

# configure Redis
from redis import Redis
redis = Redis(host=config.get('REDIS_HOST'), port=config.get('REDIS_PORT'))
