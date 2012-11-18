from _src.annt import SoftAssert as Assert
from _src.base_test_fixture import BaseTestFixture
from _src.marker import Marker

class AssertFixture(BaseTestFixture): 
    @classmethod
    def setUp(cls):
        cls.a=2
        
    @classmethod
    def setUp_class(cls):
        pass
    
    @classmethod
    def tearDown(cls):
        pass
    
class AssertTests:           
    @Marker('T2')
    def test_hello(self):
        Assert.assertEquals(AssertFixture.a,2)
        Assert.assertEquals(AssertFixture.a,10)
        
    @Marker('T1')
    def test_hello2(self):
        Assert.assertEquals(AssertFixture.a,41)
        Assert.assertEquals(AssertFixture.a,13)
