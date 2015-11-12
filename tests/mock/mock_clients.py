from application.service.model import Borrower, Address, Deed
from flask.ext.api import status


class DeedApiMockClient:
    @staticmethod
    def get_deed(deed_reference):
        address = Address("Flat 16 Kingman Court",
                          "Verdant Road",
                          "London",
                          "SV19 9BT")
        borrower = Borrower("John Andrew", address)
        title_number = 'dm1234'
        deed = Deed(
            deed_reference,
            [borrower],
            title_number
        )

        return deed
