
from flask import Flask

from views.auth import bp as auth_bp
from views.posts import bp as posts_bp
from views.home import bp as home_bp
from views.user import bp as user_bp


def createApp(config):

	app = Flask(__name__)

	app.config.from_object(config)

	app.register_blueprint(auth_bp,url_prefix="/auth")
	app.register_blueprint(posts_bp,url_prefix="/posts")
	app.register_blueprint(home_bp,url_prefix="/")
	app.register_blueprint(user_bp,url_prefix="/profile")

	return app
