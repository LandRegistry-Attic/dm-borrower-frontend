from flask import Blueprint, render_template, request
import datetime
import sys
from flask.ext.api import status
from application.deed.searchdeed.address_utils import format_address_string

searchdeed = Blueprint('searchdeed', __name__,
                       template_folder='/templates',
                       static_folder='static')


@searchdeed.route('/')
def search_deed_main():
    return render_template('searchdeed.html')


def validate_dob(form):
    error = None
    try:
        day = int(form["dob-day"])
        month = int(form["dob-month"])
        year = int(form["dob-year"])

        datetime.datetime(year, month, day)

    except:
        print(sys.exc_info()[0])
        error = "Please enter a valid date of birth"

    return error


@searchdeed.route('/enter-dob', methods=['POST'])
def enter_dob():
    form = request.form

    if 'validate' in form:
        form.error = validate_dob(form)
        if form.error is None:
            return do_search_deed_search(form)

    return render_template('enterdob.html', form=form)


@searchdeed.route('/search', methods=['POST'])
def search_deed_search():
    form = request.values
    response = do_search_deed_search(form)
    return response, status.HTTP_200_OK


def do_search_deed_search(form):
    borrower_token = form['borrower_token']

    dob = form["dob-day"] + "/" + form["dob-month"] + "/" + form["dob-year"]

    deed_token = validate_borrower(borrower_token, dob)

    deed_data = None

    if deed_token:
        deed_data = lookup_deed(deed_token['deed_token'])

    if deed_data is not None:
        deed_data["deed"]["property_address"] = format_address_string(deed_data["deed"]["property_address"])
        response = render_template('viewdeed.html', deed_data=deed_data,
                                   deed_reference=deed_token)
    else:
        response = render_template('deednotfound.html',
                                   borrower_token=borrower_token)

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
