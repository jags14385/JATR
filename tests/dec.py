from _src.annt import SoftAssert as Assert
from _src.base_test_fixture import BaseTestFixture
from _src.marker import Marker

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
    @Marker('T2')
    def test_hello(self):
        Assert.assertEquals(AssertFixture.a,241)
        Assert.assertEquals(AssertFixture.a, 1)
        
    @Marker('T1')
    def test_hello2(self):
        Assert.assertEquals(AssertFixture.a,241)
        Assert.assertEquals(AssertFixture.a, 1)

    @Marker('T1')
    def test_hello3(self):
        Assert.assertEquals(AssertFixture.a,243)
        Assert.assertEquals(AssertFixture.a, 2)
        Assert.assertEquals(AssertFixture.a,2431)