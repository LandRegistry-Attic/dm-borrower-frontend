from tests.helpers import setUpApp
import unittest
from application.deed.searchdeed import address_utils


class TestFormatAddress(unittest.TestCase):
    def setUp(self):
        setUpApp(self)

    def test_format_address(self):
        address = address_utils.format_address_string("103 street name, the town, the city,PL6 5WS")
        self.assertEqual(address, ["103 street name","the town","the city","PL6 5WS"])

    def test_format_address_with_comma_after_house_number(self):
        address = address_utils.format_address_string("103,street name, the town, the city,PL6 5WS")
        self.assertEqual(address, ["103 street name", "the town","the city","PL6 5WS"])

    def test_format_address_with_whitespace(self):
        address = address_utils.format_address_string("103 street name , the town, the city , PL6 5WS ")
        self.assertEqual(address, ["103 street name","the town","the city","PL6 5WS"])

    def test_format_address_with_post_code_in_wrong_place(self):
        address = address_utils.format_address_string("103 street name , the town, PL6 5WS ,the city")
        self.assertEqual(address, ["103 street name","the town","the city","PL6 5WS"])

    def test_format_address_lowercase_postcode(self):
        address = address_utils.format_address_string("103 street name , the town, the city, pl6 5ws")
        self.assertEqual(address, ["103 street name","the town","the city","PL6 5WS"])

    def test_format_combined(self):
        address = address_utils.format_address_string("103, street name , the town , the city , pl6 5ws ")
        self.assertEqual(address, ["103 street name","the town","the city","PL6 5WS"])
