from flask import Blueprint

general = Blueprint("general", __name__)  # initialize blueprint


# function that is called when you visit /
@general.route("/")
def index():
    return "Success" 
