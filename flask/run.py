from known.factory import create_app, register_cli

if __name__ == '__main__':
    app = create_app()
    app.run()
