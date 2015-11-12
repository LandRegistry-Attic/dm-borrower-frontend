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
        deed_api_client = getattr(searchdeed, 'deed_api_client')
        deed_data = deed_api_client.get_deed(str(deed_reference))
    else:
        deed_data = None

    return deed_data
