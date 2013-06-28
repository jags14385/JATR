from _src.annt import Verify
from _src.base_test_fixture import TestCase
from _src.marker import Marker

class AssertFixture(TestCase): 
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
            
class AssertTests:         
    @Marker('tx')
    def test_hello1(self):
        Verify.verifyEquals(AssertFixture.a, 241)
        assert 1==2
        Verify.verifyEquals(AssertFixture.a, 1012)
        
    @Marker('T1','t2','tx')
    def test_hello2(self):
        Verify.verifyEquals(AssertFixture.a, 2411)
        Verify.verifyEquals(AssertFixture.a, 1)
        
    @Marker('T1')
    def test_hello(self):
        Verify.verifyEquals(AssertFixture.list_num, AssertFixture.list_num1)