from samantha import app
from samantha.tasks import greet


@app.route('/')
def hello():
    greeting = greet.delay('world')
    greeting.wait()

    return greeting.get()
