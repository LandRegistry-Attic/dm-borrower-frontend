from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from werkzeug import exceptions
import datetime
from flask.ext.api import status
from application.deed.searchdeed.address_utils import format_address_string


searchdeed = Blueprint('searchdeed', __name__,
                       template_folder='/templates',
                       static_folder='static')


@searchdeed.route('/borrower-reference', methods=['GET', 'POST'])
def search_deed_main():
    if session.get("error"):
        session.pop("error")
        return render_template('searchdeed.html', error=True)
    else:
        session.clear()
        session.permanent = True
        return render_template('searchdeed.html', error=None)


@searchdeed.route('/date-of-birth', methods=['POST'])
def enter_dob():
    form = request.form
    form.current_year = str(datetime.datetime.now().year)

    if 'validate' in form:
        form.error = validate_dob(form)
        if form.error is None:
            dob = form["dob-day"] + "/" + form["dob-month"] + "/" + form["dob-year"]
            result = validate_borrower(form['borrower_token'], dob)
            if result is not None:
                session['deed_token'] = result['deed_token']
                session['phone_number'] = result['phone_number']
                session['borrower_token'] = form['borrower_token']
                return redirect('/how-to-proceed', code=307)
            else:
                session['error'] = "True"
                return redirect('/borrower-reference', code=307)

    return render_template('enterdob.html', form=form)


@searchdeed.route('/mortgage-deed', methods=['GET'])
def search_deed_search():
    if 'deed_token' not in session:
        return redirect('/session-ended', code=302)

    response = do_search_deed_search()
    return response, status.HTTP_200_OK


@searchdeed.route('/enter-authentication-code', methods=['GET', 'POST'])
def show_authentication_code_page():

    if 'deed_token' not in session:
        return redirect('/session-ended', code=302)

    if request.args.get('error', False):
        return render_template('authentication-code.html', error=True)

    send_auth_code()
    render_page = render_template('authentication-code.html')
    session['code-sent'] = True

    return render_page


@searchdeed.route('/confirming-mortagage-deed', methods=['POST'])
def show_confirming_deed_page():

    auth_code = request.form['auth_code']

    if auth_code is None or auth_code == '':
        return render_template('authentication-code.html', error=True)

    page_render = render_template('confirming-mortgage-deed.html', auth_code=request.form['auth_code'])
    return page_render


@searchdeed.route('/confirming-mortagage-deed-call', methods=['POST'])
def show_confirming_deed_page_call():
    auth_code = request.form['auth_code']

    if auth_code is None or auth_code == '':
        return jsonify({'error': True, 'redirect': url_for('searchdeed.show_authentication_code_page', error=True)})

    # Check to see if we've got a result back from eSecurity and return an appropriate status to the browser
    deed_api_client = getattr(searchdeed, 'deed_api_client')
    response = deed_api_client.verify_auth_code(str(session.get('deed_token')),
                                                str(session.get('borrower_token')),
                                                auth_code)

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        return jsonify({'error': True, 'redirect': url_for('searchdeed.show_authentication_code_page', error=True)})
    elif response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE or response.status_code == status.HTTP_404_NOT_FOUND:
        return jsonify({'error': True, 'redirect': url_for('searchdeed.show_internal_server_error_page')})

    return jsonify({'error': False})


@searchdeed.route('/confirming-mortagage-deed-check', methods=['GET'])
def show_confirming_deed_page_check():
    if deed_signed():
        return jsonify({'result': True, 'redirect': url_for('searchdeed.show_final_page')})
    else:
        return jsonify({'result': False})


def send_auth_code():
    deed_api_client = getattr(searchdeed, 'deed_api_client')
    response = deed_api_client.request_auth_code(str(session.get('deed_token')), str(session.get('borrower_token')))

    if response.status_code != status.HTTP_200_OK:
        session['service_timeout_at_send_code'] = True
        raise exceptions.ServiceUnavailable


@searchdeed.route('/finished', methods=['GET', 'POST'])
def show_final_page():
    session.clear()
    return render_template('finished.html')


@searchdeed.route('/session-ended', methods=['GET'])
def session_ended():
    return render_template('session-ended.html')


@searchdeed.route('/service-unavailable/deed-not-confirmed')
def show_internal_server_error_page():
    return render_template('deed-not-confirmed.html')


@searchdeed.errorhandler(status.HTTP_503_SERVICE_UNAVAILABLE)
def internal_server_error(e):
    return redirect(url_for('searchdeed.show_internal_server_error_page'))


def validate_dob(form):
    error = None
    try:
        present = datetime.datetime.now()

        day = int(form["dob-day"])
        month = int(form["dob-month"])
        year = int(form["dob-year"])

        dob_date = datetime.datetime(year, month, day)

        if dob_date >= present:
            raise Exception("Date cannot be in the future")

    except:
        error = "Please enter a valid date of birth"

    return error


def validate_borrower(borrower_token, dob):
    if borrower_token is not None and borrower_token != '':
        payload = {
            "borrower_token": borrower_token,
            "dob": str(dob)
            }
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        result = deed_api_client.validate_borrower(payload)
        return result


def do_search_deed_search():
    deed_data = lookup_deed(session['deed_token'])
    if deed_data is not None:
        deed_data["deed"]["property_address"] = format_address_string(deed_data["deed"]["property_address"])
        if deed_signed():
            response = render_template('viewdeed.html', deed_data=deed_data, signed=True)
        else:
            response = render_template('viewdeed.html', deed_data=deed_data, signed=False)
    else:
        return render_template('searchdeed.html', error=True)

    return response


def lookup_deed(deed_reference):
    if deed_reference is not None and deed_reference != '':
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        deed_data = deed_api_client.get_deed(str(deed_reference))
    else:
        deed_data = None

    return deed_data


def deed_signed():
    deed_data = lookup_deed(session['deed_token'])
    if deed_data is not None:
        for borrower in deed_data['deed']['borrowers']:
            if 'signature' in borrower and borrower['token'] == session.get('borrower_token'):
                return True
