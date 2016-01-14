from flask import Blueprint, render_template, request

searchdeed = Blueprint('searchdeed', __name__,
                       template_folder='/templates',
                       static_folder='static')


@searchdeed.route('/')
def search_deed_main():
    return render_template('searchdeed.html')


@searchdeed.route('/search', methods=['POST'])
def search_deed_search():
    borrower_token = request.form['borrower_token']

    deed_token = validate_borrower(borrower_token)

    deed_data = None

    if deed_token:
        deed_data = lookup_deed(deed_token['deed_token'])

    if deed_data is not None:
        response = render_template('viewdeed.html', deed_data=deed_data,
                                   deed_reference=deed_token)
    else:
        response = render_template('deednotfound.html',
                                   borrower_token=borrower_token)

    return response


def validate_borrower(borrower_token):
    if borrower_token is not None and borrower_token != '':
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        deed_token = deed_api_client.validate_borrower(str(borrower_token))
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
