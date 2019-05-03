"""AppFactory"""
import flask

from .bp_index import auto_bp

UPLOAD_FOLDER = "uploads/"


def create_app():
    """Create an app"""
    app = flask.Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.register_blueprint(auto_bp, url_prefix="/teachers/4yrplan")

    with app.app_context():
        # pylint: disable=unused-import
        from . import index  # noqa: E402, F401
        from . import students  # noqa: E402, F401
        from . import teachers  # noqa: E402, F401
        from . import login  # noqa: E402, F401
    return app
