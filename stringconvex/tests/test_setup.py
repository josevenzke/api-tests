from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.token_url = reverse('token_obtain_pair')
        user = User.objects.create_user(username='testuser',password='12345')
        user.save()

        self.login_data={
            'username':"testuser",
            'password':"12345"
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
