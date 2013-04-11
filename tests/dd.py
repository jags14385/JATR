from _src.base_test_fixture import TestCase
from _src.data_marker import DataMarker
from _src.annt import Verify
class Assert23Fixture(TestCase): 
    @classmethod
    def setup(cls):
        cls.a = 2
        cls.list_num = [1, 2, 3]
        cls.list_num1 = [1, 2, 3]
                
    @classmethod
    def setup_class(cls):
        pass
        
    @classmethod
    def teardown(cls):
        pass
            
class Assert23Tests:         
        
    @DataMarker(data_args=[1,2,3])
    def test_hello(self,num_arg):
        Verify.verifyEquals(1,num_arg)
        print "Data"