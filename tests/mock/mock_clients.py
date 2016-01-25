from application.service.model import Borrower, Address, Deed


class DeedApiMockClient:
    @staticmethod
    def get_deed(deed_reference):
        address = Address("Flat 16 Kingman Court",
                          "Verdant Road",
                          "London",
                          "SV19 9BT")
        borrower = Borrower("John Andrew", address)
        title_number = 'dm1234',
        lender = {
            "name": "Bank of England",
            "address":"address",
            "registration":"company registration"
        }
        charge_clause = { "description":"a charge clause"}

        additional_provisions = [ { "description":"provision 1"}]

        deed = Deed(
            deed_reference,
            [borrower],
            title_number,
            lender,
            charge_clause,
            additional_provisions
        )

        return {"deed": deed}

    @staticmethod
    def validate_borrower(borrower_token):
        deed_token = "aaaaaaa"

        return {"deed_token": deed_token}
