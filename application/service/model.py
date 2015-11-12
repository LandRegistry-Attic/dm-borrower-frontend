class Deed:
    def __init__(self, deed_reference, borrowers, title_number):
        self.deed_reference = deed_reference
        self.borrowers = borrowers
        self.title_number = title_number


class Borrower:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Address:
    def __init__(self, street, extended, locality, postal_code):
        self.street_address = street
        self.extended_address = extended
        self.locality = locality
        self.postal_code = postal_code
