""" Advisagator Application in Flask """
import os

# pylint: disable=W0611
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

import login_handler
import database_handler


# pylint: disable=C0103
app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/", methods=["GET"])
def home_redirect():
    """ Displays the home page accessible at '/' """
    return redirect("/home")


@app.route("/home", methods=["GET"])
def home_get():
    """ Displays the home page or redirects to /petitions """
    # pylint: disable=R1705
    if not session.get("logged_in"):
        return render_template("home.html")
    else:
        return redirect("/petitions")


@app.route("/login", methods=["GET"])
def login_get():
    """ Displays the login page or redirects to /petitions """
    # pylint: disable=R1705
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return redirect("/petitions")


@app.route("/login", methods=["POST"])
def login_post():
    """ Checks the information for email and password then directs to /petitions """
    email = request.form["email"]
    password = request.form["password"]
    valid = login_handler.validate_user(email, password)
    # pylint: disable=R1705
    if valid:
        session["logged_in"] = True
        session["email"] = email
        return redirect("/petitions")
    else:
        return redirect("/invalid_login")


@app.route("/invalid_login", methods=["GET"])
def invalid_login_get():
    """  Displays invalid_login.html accessible at '/invalid_login' """
    return render_template("invalid_login.html")


@app.route("/logout", methods=["GET"])
def logout_get():
    """ Clears session and displays '/home' """
    session.clear()
    return redirect("/home")


@app.route("/change_password", methods=["GET"])
def change_password_get():
    """ Displays the change password page or redirects to '/home' """
    # pylint: disable=R1705
    if session.get("logged_in"):
        return render_template("change_password.html")
    else:
        return redirect("/home")


@app.route("/change_password", methods=["POST"])
def change_password_post():
    """ Allows user to modify exisiting information for the login password """
    # pylint: disable=R1705
    if session.get("logged_in"):
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password == confirm_password:
            # database_handler.update_password(session.get('email'), new_password)
            print(password)
            return redirect("/petitions")
        else:
            return redirect("/invalid_confirmation")
    else:
        return redirect("/home")


@app.route("/invalid_confirmation", methods=["GET"])
def invalid_confirmation_get():
    """ Displays the invalid_confirmation.html if logged_in or redirects to /home """
    # pylint: disable=R1705
    if session.get("logged_in"):
        return render_template("invalid_confirmation.html")
    else:
        return redirect("/home")


@app.route("/petitions", methods=["GET"])
def petitions_get():
    """ Displays 'petitions.html' or redirects to '/home' """
    # pylint: disable=R1705
    if session.get("logged_in"):
        petitions = database_handler.get_petitions(session["email"])
        out_petitions = list()
        for petition in petitions:
            new_petition = {
                "id": petition[3],
                "name": petition[0],
                "email": petition[1],
                "department": petition[2],
            }
            out_petitions.append(new_petition)
        return render_template("petitions.html", petitions=out_petitions)
    else:
        return redirect("/home")


@app.route("/petitions/<id>", methods=["GET"])
def petitions_inspect_get(did):
    """ Displays petition info if logged in or redirects to '/home' """
    # pylint: disable=R1705
    if session.get("logged_in"):
        petition = database_handler.get_petition_info(did)
        new_petition_info = {
            "id": petition[4],
            "name": petition[0],
            "email": petition[1],
            "department": petition[3],
            "content": petition[2],
        }
        return render_template("petition_info.html", petition_info=new_petition_info)
    else:
        return redirect("/home")


@app.route("/petitions/<id>", methods=["POST"])
def petitions_inspect_post():
    """ Allows the user access to '/petition' if approved or redirects to '/home' """
    # pylint: disable=R1705
    if session.get("logged_in"):
        approved = request.form["approved"]
        print(approved)
        return redirect("/petitions")
    else:
        return redirect("/home")


@app.errorhandler(404)
def page_not_found():
    """ Method for 404 error handling """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
