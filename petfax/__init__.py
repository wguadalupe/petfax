from flask import Flask

# factory
def create_app():
    # existing code to create the Flask app
    app = Flask(__name__)

    # existing routes and app configuration
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # return the app
    return app
