from quart import Quart


def create_app():
    app = Quart(__name__)
    return app

