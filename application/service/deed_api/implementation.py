import requests
from application import config
from flask.ext.api import status


def get_deed(deed_reference):  # pragma: no cover
    data = None
    resp = requests.get(config.DEED_API_BASE_HOST + '/deed/' +
                        str(deed_reference))

    if resp.status_code == status.HTTP_200_OK:
        data = resp.json()

    return data


def validate_borrower(payload):  # pragma: no cover
    resp = requests.post(config.DEED_API_BASE_HOST +
                         '/borrower/validate', json=payload)
    deed_token = None
    if resp.status_code == status.HTTP_200_OK:
        deed_token = resp.json()

    return deed_token


def add_borrower_signature(deed_reference, borrower_token):
    response = requests.post(config.DEED_API_BASE_HOST +
                             '/deed/' + deed_reference + '/sign', json=borrower_token)
    return response
