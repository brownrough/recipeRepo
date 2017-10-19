from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/css')
        self.assertEqual(response.status_code, 200)

    def test_signin_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signIn', content_type='html/css')
        self.assertTrue(b"Login" in response.data)
    def test_signup_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signUp', content_type='html/css')
        self.assertEqual(response.status_code, 200)

    def test_category_loads(self):
        tester = app.test_client(self)
        response = tester.get('/categories', content_type='html/css')
        self.assertEqual(response.status_code, 200)

    def test_recipe_loads(self):
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/css')
        self.assertEqual(response.status_code, 200)
    


if __name__ == 'main':
    unittest.main()
