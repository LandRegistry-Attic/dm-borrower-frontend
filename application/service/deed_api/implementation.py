import requests
from application import config
from flask.ext.api import status


def get_deed(deed_reference):
    data = None
    resp = requests.get(config.DEED_API_BASE_HOST + '/deed/' +
                        str(deed_reference))

    if resp.status_code == status.HTTP_200_OK:
        data = resp.json()

    return data


def validate_borrower(borrower_token):
    data = None
    resp = requests.get(config.DEED_API_BASE_HOST + '/borrower/' +
                        str(borrower_token))

    if resp.status_code == status.HTTP_200_OK:
        data = resp.json()

    return data
