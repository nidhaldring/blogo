



from flask import Flask 

from views.auth import bp as auth_bp
from views.posts import bp as posts_bp


def createApp(config):

	app = Flask(__name__)

	app.config.from_object(config)

	app.register_blueprint(auth_bp,url_prefix="/auth")
	app.register_blueprint(posts_bp,url_prefix="/posts")

	return app
