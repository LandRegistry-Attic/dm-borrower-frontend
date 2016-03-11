from flask import Blueprint, render_template, Response, request, session, redirect
from application import config

borrower_landing = Blueprint('borrower_landing', __name__,
                             template_folder='/templates',
                             static_folder='static')


@borrower_landing.route('/how-to-proceed', methods=['POST'])
def verified():
    return render_template('howtoproceed.html')


@borrower_landing.route('/sign-my-mortgage')
def home():
    return render_template("start.html")


@borrower_landing.route('/start')
def start():
    if config.VERIFY:
        return redirect('/identity-verified', code=307)
    else:
        return redirect('/borrower-reference', code=307)


@borrower_landing.route('/identity-verified', methods=['GET'])
def identity_verified():
    if 'deed_token' not in session:
        return Response('Unauthenticated', 401, {'WWW-Authenticate': 'Basic realm="Authentication Required"'})
    else:
        return render_template("identity-verified.html")


@borrower_landing.route('/verify', methods=['POST'])
def verify_identity():
    if 'Pid' in request.headers:
        # TODO: Update this to perform a lookup using the pid
        session['deed_token'] = 'e63eb5'

    return redirect('/identity-verified', code=302)
