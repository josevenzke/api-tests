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

        self.array_data={
            'array':'4,6,3,8,2,10,23,1,93,92'
        }
        self.array_sorted = [1,2,3,4,6,8,10,23,92,93]

        self.quicksort = reverse('quicksort')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_token_no_data(self):
        res = self.client.post(self.token_url)
        self.assertEqual(res.status_code,400)
    
    def test_get_token(self):
        res = self.client.post(self.token_url, self.login_data)
        self.assertEqual(res.status_code,200)