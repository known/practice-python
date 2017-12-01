import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask('known')

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'known.db'),
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})
    app.config.from_envvar('KNOWN_SETTINGS', silent=True)

    register_blueprints(app)
    register_cli(app)
    register_teardowns(app)

    return app


def register_blueprints(app):
    for name in find_modules('known.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    #@app.cli.command('initdb')
    #def initdb_command():
    for name in find_modules('known.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'init_db'):
            mod.init_db()
            print('Initialized the %s database.' % name)


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'db'):
            g.db.close()
