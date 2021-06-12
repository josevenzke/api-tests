from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.token_url = reverse('token_obtain_pair')
        self.quicksort = reverse('quicksort')

        self.login_data={
            'username':"admin",
            'password':"admin",
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()