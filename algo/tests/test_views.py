from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):

    def test_algo_quicksort(self):     
        res = self.client.post(self.quicksort,self.array_data)
        sort = res.data.get('sorted_array')

        self.assertEqual(sort,self.array_sorted)