from .test_setup import TestSetUp
import pdb

class Testlogin(TestSetUp):

    def test_token_no_data(self):
        response = self.client.post(self.token_url)
        
        self.assertEqual(response.status_code,400)
    
    def test_get_token(self):
        response = self.client.post(self.token_url, self.login_data)
        self.assertEqual(response.status_code,200)