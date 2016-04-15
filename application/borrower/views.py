from flask import Blueprint, render_template

borrower_landing = Blueprint('borrower_landing', __name__,
                             template_folder='/templates',
                             static_folder='static')


@borrower_landing.route('/how-to-proceed', methods=['POST'])
def verified():
    return render_template('howtoproceed.html')


@borrower_landing.route('/')
def home():
    return render_template("start.html")
