from flask import Blueprint, render_template, request

borrower_landing = Blueprint('borrower_landing', __name__,
                             template_folder='/templates',
                             static_folder='static')


@borrower_landing.route('/how-to-proceed', methods=['POST'])
def verified():
    form = request.form
    dob = form["dob-day"] + "/" + form["dob-month"] + "/" + form["dob-year"]
    borrower_token = request.form['borrower_token']
    return render_template('howtoproceed.html', borrower_token=borrower_token,
                           dob=dob)


@borrower_landing.route('/sign-my-mortgage')
def home():
    return render_template("start.html")
