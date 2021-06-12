from .test_setup import TestSetUp

class TestViews(TestSetUp):

    def test_token_no_data(self):
        res = self.client.post(self.token_url)
        self.assertEqual(res.status_code,400)
    
    def test_get_token(self):
        res = self.client.post(self.token_url, self.login_data, content_type='x-www-form-urlencoded')
        import pdb
        pdb.set_trace()
        self.assertEqual(res.status_code,200)