from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    
    def setUp(self):
        self.quicksort = reverse('quicksort')
        self.quicksort_array_data={
            'array':'4,6,3,8,2,10,23,1,93,92'
        }
        self.quicksort_result = [1,2,3,4,6,8,10,23,92,93]


        self.binary_search = reverse('binary-search')
        self.binary_search_array_data={
            'array':'1,2,3,5,7,8,21,35,36,97,203,504,607',
            'item':'3'
        }
        self.binary_search_result = 2

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
