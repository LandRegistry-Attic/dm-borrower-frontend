from flask import Blueprint, render_template

borrower_landing = Blueprint('borrower_landing', __name__,
                   template_folder='/templates',
                   static_folder='static')


@borrower_landing.route('/')
def home():
    return render_template("landing.html")
