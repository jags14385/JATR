from _src.annt import SoftAssert as Assert
from _src.base_test_fixture import BaseTestFixture

class AssertFixture(BaseTestFixture): 
    @classmethod
    def setUp(cls):
        cls.a=2
        print "Setup method Test Level /Method Level"
        
    @classmethod
    def setUp_class(cls):
        print "Setup method Class Level"
        
    @classmethod
    def tearDown(cls):
        print "TearDown method Test Level /Method Level"
        
class AssertTests:           
    @Assert    
    def test_hello(self):
        Assert.assertEquals(AssertFixture.a, 241)
        Assert.assertEquals(AssertFixture.a, 1)