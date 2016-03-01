import requests
from application import config
from flask.ext.api import status

webseal_headers = {
    "Content-Type": "application/json",
    "Iv-User-L": "CN=DigitalMortgage%20DigitalMortgage,OU=devices,O=Land%20Registry%20Internal,O=*,C=gb"
}


def get_deed(deed_reference):  # pragma: no cover
    data = None
    resp = requests.get(config.DEED_API_BASE_HOST + '/deed/' +
                        str(deed_reference),
                        headers=webseal_headers)

    if resp.status_code == status.HTTP_200_OK:
        data = resp.json()

    return data


def validate_borrower(payload):  # pragma: no cover
    resp = requests.post(config.DEED_API_BASE_HOST +
                         '/borrower/validate', json=payload,
                         headers=webseal_headers)
    if resp.status_code == status.HTTP_200_OK:
        return resp.json()


def add_borrower_signature(deed_reference, borrower_token):
    response = requests.post(config.DEED_API_BASE_HOST +
                             '/deed/' + deed_reference + '/sign', json=borrower_token, headers=webseal_headers)
    return response


def send_sms(deed_reference, borrower_token):
    payload = {"borrower_token": borrower_token}
    response = requests.post(config.DEED_API_BASE_HOST +
                             '/deed/' + deed_reference + '/send-sms', json=payload, headers=webseal_headers)
    return response


def verify_sms(deed_reference, borrower_token, authentication_code):
    payload = {"borrower_token": borrower_token, "authentication_code": authentication_code}
    response = requests.post(config.DEED_API_BASE_HOST +
                             '/deed/' + deed_reference + '/verify-sms', json=payload, headers=webseal_headers)
    return response
