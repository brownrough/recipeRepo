from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/signIn', content_type='html/css')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signIn', content_type='html/css')
        self.assertTrue(b"Login" in response.data)
    #correct creditials behavious

    #Incorrect credetials

    # #Logout behaviour


if __name__ == 'main':
    unittest.main()
