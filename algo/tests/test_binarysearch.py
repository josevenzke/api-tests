from algo.views import quicksort_sort
from .test_setup import TestSetUp
import pdb

class TestBinarySearch(TestSetUp):

    def test_algo_binary_search(self):
        response = self.client.post(self.binary_search,self.binary_search_array_data)
        item_index = response.data.get('item_index')

        self.assertEqual(item_index,self.binary_search_result)

    def test_algo_binary_search_no_data(self):
        response = self.client.post(self.binary_search)
        error_message = response.data.get('detail')

        self.assertEqual(error_message,'Parametros insuficientes')

    def test_algo_binary_search_wrong_dataype(self):
        response = self.client.post(self.binary_search,{'array':'[asda,ew]','item':4})
        error_message = response.data.get('detail')

        self.assertEqual(error_message,'Parametros invalidos')