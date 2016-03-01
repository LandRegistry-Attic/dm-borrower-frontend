class DeedApiInterface(object):  # pragma: no cover
    def __init__(self, implementation):
        self.implementation = implementation

    def get_deed(self, deed_reference):
        return self.implementation.get_deed(deed_reference)

    def validate_borrower(self, payload):
            return self.implementation.validate_borrower(payload)

    def add_borrower_signature(self, deed_reference, borrower_token):
        return self.implementation.add_borrower_signature(deed_reference, borrower_token)

    def send_sms(self, deed_reference, borrower_token):
        return self.implementation.send_sms(deed_reference, borrower_token)

    def verify_sms(self, deed_reference, borrower_token, authentication_code):
        return self.implementation.verify_sms(deed_reference, borrower_token, authentication_code)
