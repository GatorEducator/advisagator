""" This is undocumented """
from flask import (
    render_template,
    Flask,
    Response,
    redirect,
    url_for,
    request,
    abort,
    session,
)
import os
import login_handler

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/", methods=["GET"])
def home_redirect():
    """ This is undocumented """
    return redirect("/home")


@app.route("/home", methods=["GET"])
def home_get():
    """ This is undocumented """
    if not session.get("logged_in"):
        return render_template("home.html")
    else:
        return redirect("/petitions")
        # pylint: disable=no-else-return


@app.route("/login", methods=["GET"])
def login_get():
    """ This is undocumented """
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return redirect("/petitions")
        # pylint: disable=no-else-return


@app.route("/login", methods=["POST"])
def login_post():
    """ This is undocumented """
    email = request.form["email"]
    password = request.form["password"]
    valid = login_handler.validate_user(email, password)
    if valid:
        session["logged_in"] = True
        session["email"] = email
        return redirect("/petitions")
    else:
        return redirect("/invalid_login")
        # pylint: disable=no-else-return


@app.route("/invalid_login", methods=["GET"])
def invalid_login_get():
    """ This is undocumented """
    return render_template("invalid_login.html")


@app.route("/logout", methods=["GET"])
def logout_get():
    """ This is undocumented """
    session.clear()
    return redirect("/home")


@app.route("/petitions", methods=["GET"])
def petitions_get():
    """ This is undocumented """
    if session.get("logged_in"):
        return render_template("petitions.html")
    else:
        return redirect("/home")
        # pylint: disable=no-else-return


@app.errorhandler(404)
def page_not_found(e):
    """ This is undocumented """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
