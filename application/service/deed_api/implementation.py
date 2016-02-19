import requests
from application import config
from flask.ext.api import status

webseal_headers = {
    "Content-Type": "application/json",
    "Iv-User-L":"CN=DigitalMortgage%20DigitalMortgage,OU=devices,O=Land%20Registry%20Internal,O=*,C=gb"
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
    deed_token = None
    if resp.status_code == status.HTTP_200_OK:
        deed_token = resp.json()

    return deed_token
