from flask import Blueprint, render_template, request

searchdeed = Blueprint('searchdeed', __name__,
                       template_folder='/templates',
                       static_folder='static')


@searchdeed.route('/')
def search_deed_main():
    return render_template('searchdeed.html')


@searchdeed.route('/search', methods=['POST'])
def search_deed_search():
    deed_reference = request.form['deed_reference']

    deed_data = lookup_deed(deed_reference)

    if deed_data is not None:
        response = render_template('viewdeed.html', deed_data=deed_data,
                                   deed_reference=deed_reference)
    else:
        response = render_template('deednotfound.html',
                                   deed_reference=deed_reference)

    return response


def lookup_deed(deed_reference):
    if deed_reference is not None and deed_reference != '':
        # TODO: fire off request to deed API here ...
        deed_data = {
            'borrowers': [
                {'first_name': 'fred', 'last_name': 'bloggs'},
                {'first_name': 'mickey', 'last_name': 'mouse'}
            ],
            'property': {
                'address': 'disney land, florida'
            },
            'title_reference': 'ref-1234a',
            'deed_reference': deed_reference
        }
    else:
        deed_data = None

    return deed_data
