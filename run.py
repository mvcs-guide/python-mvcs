import os

from samantha import app, config
import samantha.views


if __name__ == "__main__":
    app.run(
        host=config.get('FLASK_HOST'),
        debug=config.get('FLASK_IS_DEBUG')
    )
