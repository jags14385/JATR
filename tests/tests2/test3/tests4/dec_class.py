from _src.annt import SoftAssert as Assert
from _src.base_test_fixture import BaseTestFixture

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
    @Assert    
    def test_hello(self):
        Assert.assertEquals(AssertFixture.a, 721)
        Assert.assertEquals(AssertFixture.a, 231)