import requests

from application import config

DEED_API_BASE_HOST = config.DEED_API_BASE_HOST

def get_deed_json(borrower_token):
    return requests.get(DEED_API_BASE_HOST + '/deed/borrower/' +
                        str(borrower_token)).json()

def get_deed(borrower_token):

    deed_json = get_deed_json(borrower_token)

    return deed_json
