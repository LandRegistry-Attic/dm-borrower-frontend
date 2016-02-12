from flask import Blueprint, render_template, request, redirect, session
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
        return render_template('searchdeed.html', error=None)


@searchdeed.route('/finished', methods=['POST'])
def show_final_page():
    session.clear()
    return render_template('finished.html')


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


@searchdeed.route('/date-of-birth', methods=['POST'])
def enter_dob():
    form = request.form
    form.current_year = str(datetime.datetime.now().year)

    if 'validate' in form:
        form.error = validate_dob(form)
        if form.error is None:
            dob = form["dob-day"] + "/" + form["dob-month"] + "/" + form["dob-year"]
            deed_token = validate_borrower(form['borrower_token'], dob)
            if deed_token is not None:
                session['deed_token'] = deed_token['deed_token']
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


@searchdeed.route('/session-ended', methods=['GET'])
def session_ended():
    return render_template('session-ended.html')


def do_search_deed_search():

    deed_data = lookup_deed(session['deed_token'])

    if deed_data is not None:
        deed_data["deed"]["property_address"] = format_address_string(deed_data["deed"]["property_address"])
        response = render_template('viewdeed.html', deed_data=deed_data)

    else:
        return render_template('searchdeed.html', error=True)

    return response


def validate_borrower(borrower_token, dob):
    if borrower_token is not None and borrower_token != '':
        payload = {
            "borrower_token": borrower_token,
            "dob": str(dob)
            }
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        deed_token = deed_api_client.validate_borrower(payload)
    else:
        deed_token = None

    return deed_token


def lookup_deed(deed_reference):
    if deed_reference is not None and deed_reference != '':
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        deed_data = deed_api_client.get_deed(str(deed_reference))
    else:
        deed_data = None

    return deed_data
