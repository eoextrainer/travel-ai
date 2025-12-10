import os
import unittest
from connectors import test_amadeus, test_skyscanner, test_yelp, test_google_places

class TestConnectors(unittest.TestCase):
    def test_env_keys_presence(self):
        # Keys may be empty; ensure functions return structured result
        r1 = test_amadeus().to_dict()
        r2 = test_skyscanner().to_dict()
        r3 = test_yelp().to_dict()
        r4 = test_google_places().to_dict()
        for r in (r1, r2, r3, r4):
            self.assertIn('provider', r)
            self.assertIn('ok', r)
            self.assertIn('status_code', r)
            self.assertIn('message', r)

    def test_yelp_google_optional(self):
        # If keys set, calls should attempt network
        if os.getenv('YELP_API_KEY'):
            r = test_yelp().to_dict()
            self.assertIsInstance(r['ok'], bool)
        if os.getenv('GOOGLE_PLACES_API_KEY'):
            r = test_google_places().to_dict()
            self.assertIsInstance(r['ok'], bool)

if __name__ == '__main__':
    unittest.main()
