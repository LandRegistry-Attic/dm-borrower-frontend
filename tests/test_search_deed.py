from tests.helpers import with_client, setUpApp, with_context
import unittest
from application.deed.searchdeed.views import validate_dob
from datetime import date


class TestSearchDeed(unittest.TestCase):
    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_search_deed_post(self, client):
        with client.session_transaction() as sess:
            sess['deed_token'] = '063604'

        res = client.get('/mortgage-deed')

        self.assertEqual(res.status_code, 200)

    @with_context
    @with_client
    def test_search_deed_post_invalid_reference(self, client):
        with client.session_transaction() as sess:
            sess['deed_token'] = '063604'

        res = client.get('/mortgage-deed')

        self.assertEqual(res.status_code, 200)

    @with_context
    @with_client
    def test_sign_my_mortgage_landing(self, client):
        res = client.get('/sign-my-mortgage')

        self.assertEqual(res.status_code, 200)

    @with_context
    def test_validate_dob_future(self):
        form = {
            "dob-day": "01",
            "dob-month": "01",
            "dob-year": date.today().year + 1
        }
        dobResult = validate_dob(form)
        self.assertEqual(dobResult, "Please enter a valid date of birth")

    @with_context
    def test_validate_dob(self):
        form = {
            "dob-day": "01",
            "dob-month": "01",
            "dob-year": date.today().year - 1
        }
        dobResult = validate_dob(form)
        self.assertEqual(dobResult, None)
