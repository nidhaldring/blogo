



from flask import Flask 

from auth import bp as auth_bp


def createApp(config):

	app = Flask(__name__)

	app.config.from_object(config)

	app.register_blueprint(auth_bp,url_prefix="/auth")

	return app
