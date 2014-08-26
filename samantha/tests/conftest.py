import pytest


@pytest.yield_fixture(scope='function')
def app(request):
    """Get new Flask app_context per test-run"""

    from samantha import app

    app.config['TESTING'] = True

    ctx = app.app_context()
    ctx.push()

    import samantha.views  # noqa

    yield app

    ctx.pop()


@pytest.fixture(scope='function')
def session(request):
    """Get new SQLAlchemy session per test"""

    from samantha import session, Base, engine
    import samantha.models  # noqa

    session.remove()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    return session
