from algo.views import quicksort_sort
from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):

    def test_algo_quicksort_no_data(self):
        response = self.client.post(self.quicksort)
        
        self.assertEqual(response.data.get('Success'),False)

    def test_algo_quicksort(self):     
        response = self.client.post(self.quicksort,self.quicksort_array_data)
        quicksort_array = response.data.get('sorted_array')

        self.assertEqual(quicksort_array,self.quicksort_result)
    
    def test_algo_binary_search_no_data(self):
        response = self.client.post(self.binary_search)

        self.assertEqual(response.data.get('Success'),False)


    def test_algo_binary_search(self):
        response = self.client.post(self.binary_search,self.binary_search_array_data)
        item_index = response.data.get('item_index')

        self.assertEqual(item_index,self.binary_search_result)