class DeedApiMockClient:
    @staticmethod
    def get_deed(deed_reference):
        borrowers = [
            {"forename": "John", "surname": "Andrew", "address": "30, borrower address, borrower street, city, the town, SW06 PL4"}
        ]
        title_number = 'dm1234',
        lender = {
            "name": "Bank of England",
            "address": "address",
            "registration": "company registration"
        }
        charge_clause = {"description": "a charge clause"}
        identity_checked = "Y"
        additional_provisions = [{"description": "provision 1"}]
        property_address = "30, the address, the street, the city, the town, SW06 PL4"

        deed = {
            "deed_reference": deed_reference,
            "borrowers": borrowers,
            "title_number": title_number,
            "lender": lender,
            "charge_clause": charge_clause,
            "additional_provision": additional_provisions,
            "identity_checked": identity_checked,
            "property_address": property_address
        }

        return {"deed": deed}

    @staticmethod
    def validate_borrower(payload):
        deed_token = "aaaaaaa"

        return {"deed_token": deed_token}
