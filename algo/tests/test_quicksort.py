from .test_setup import TestSetUp

class TestQuicksort(TestSetUp):

    def test_algo_quicksort(self):     
        response = self.client.post(self.quicksort,self.quicksort_array_data)
        quicksort_array = response.data.get('sorted_array')

        self.assertEqual(quicksort_array,self.quicksort_result)
    
    def test_algo_quicksort_no_data(self):
        response = self.client.post(self.quicksort)
        error_message = response.data.get('detail')

        self.assertEqual(error_message,'Parametros insuficientes')

    def test_algo_quicksort_wrong_datatype(self):
        response = self.client.post(self.quicksort,{'array':'1jjj'})
        error_message = response.data.get('detail')

        self.assertEqual(error_message,'Parametros invalidos')
