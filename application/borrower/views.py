from flask import Blueprint, render_template, request, session

borrower_landing = Blueprint('borrower_landing', __name__,
                             template_folder='/templates',
                             static_folder='static')


@borrower_landing.route('/how-to-proceed', methods=['POST'])
def verified():
    print("yo")
    print("borrower-token = %s" % session['borrower-token'])
    print("dob = %s" % session['dob'])

    print("form data for borrower-token = %s" % request.form['borrower_token'])
    return render_template("howtoproceed.html")


@borrower_landing.route('/sign-my-mortgage')
def home():
    return render_template("start.html")
