from flask import Blueprint, render_template, Response, request, session, redirect

borrower_landing = Blueprint('borrower_landing', __name__,
                             template_folder='/templates',
                             static_folder='static')


@borrower_landing.route('/how-to-proceed', methods=['POST'])
def verified():
    return render_template('howtoproceed.html')


@borrower_landing.route('/sign-my-mortgage')
def home():
    return render_template("start.html")


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
    else:
        return redirect('/verify-error', code=302)


@borrower_landing.route('/verify-error', methods=['GET'])
def verify_error():
    return render_template('verify-error.html')
