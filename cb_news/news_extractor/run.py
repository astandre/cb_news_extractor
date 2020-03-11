from cb_news.news_extractor.app import create_app
from cb_news.news_extractor.database import *
import os


def main():
    app = create_app()
    host = app.config.get('host', '0.0.0.0')
    port = app.config.get('port', 5000)
    debug = app.config.get('DEBUG', False)

    db.init_app(app)
    db.app = app
    db.create_all(app=app)

    app.run(debug=debug, host=host, port=port, use_reloader=debug)


if __name__ == "__main__":
    main()
else:
    _HERE = os.path.dirname(__file__)
    _SETTINGS = os.path.join(_HERE, 'settings.ini')
    app = create_app(settings=_SETTINGS)
    db.init_app(app)
    db.app = app
    db.create_all(app=app)
