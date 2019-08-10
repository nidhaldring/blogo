

from views.auth.utils import getCurrentUser
from views.home import bp


@bp.route("/")
def index():

	u = getCurrentUser() or ""
	return "welcome " + str(u)