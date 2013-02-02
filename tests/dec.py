from _src.annt import Verify
from _src.base_test_fixture import TestCase
from _src.marker import Marker
from _src.constants import Constants

class AssertFixture(TestCase): 
    @classmethod
    def setup(cls):
        cls.a = 2
        cls.list_num = [1, 2, 3]
        cls.list_num1 = [1, 2, 3]
        setattr(Constants,'Exper',"gsgjh")
        
    @classmethod
    def setup_class(cls):
        pass
        
    @classmethod
    def teardown(cls):
        pass
            
class AssertTests:         
    @Marker('T2')
    def test_hello(self):
        Verify.verifyEquals(AssertFixture.a, 241)
        Verify.verifyEquals(AssertFixture.a, 1)
        
    @Marker('T1')
    def test_hello2(self):
        Verify.verifyEquals(AssertFixture.a, 2411)
        Verify.verifyEquals(AssertFixture.a, 1)
        Verify.verifyEquals(AssertFixture.a, 11)
        
    @Marker('T1')
    def test_hello3(self):
        Verify.verifyEquals(AssertFixture.list_num, AssertFixture.list_num1)
