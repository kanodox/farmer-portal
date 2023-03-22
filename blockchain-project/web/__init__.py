import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="test",
        DATABASE=os.path.join(app.instance_path, 'db.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from . import db_handler
    from . import auth
    from . import items
    db_handler.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(items.bp)
    @app.route('/')
    def index():
        db = db_handler.get_db()

        items = db.execute("SELECT * FROM chain_data").fetchall()

        return render_template('index.html', items=items)
    return app