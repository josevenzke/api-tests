from algo.views import quicksort_sort
from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):

    def test_algo_quicksort(self):     
        response = self.client.post(self.quicksort,self.quicksort_array_data)
        quicksort_array = response.data.get('sorted_array')

        self.assertEqual(quicksort_array,self.quicksort_result)