from _src.annt import Verify
from _src.base_test_fixture import BaseTestFixture
from _src.marker import Marker
from _src.parametrize import Param

class AssertFixture(BaseTestFixture): 
    @classmethod
    def setUp(cls):
        cls.a = 2
        cls.list_num = [1, 2, 3]
#        print "Setup method Test Level /Method Level"
        
    @classmethod
    def setUp_class(cls):
        pass
#        print "Setup method Class Level"
        
    @classmethod
    def tearDown(cls):
        pass
#        print "TearDown method Test Level /Method Level"
        
class AssertTests:         
    @Marker('T2')
    def test_hello(self):
        Verify.verifyEquals(AssertFixture.a, 241)
        Verify.verifyEquals(AssertFixture.a, 1)
        
    @Marker('T2')
    def test_hello2(self):
        Verify.verifyEquals(AssertFixture.a, 241)
        Verify.verifyEquals(AssertFixture.a, 1)
    
    @Marker('T1')
    def test_hello3(self):
        Verify.verifyEquals(AssertFixture.a, 243)
        Verify.verifyEquals(AssertFixture.a, 2)
        Verify.verifyEquals(AssertFixture.a, 2431)

    @Param("hk")
    def test_hello4(self):
        print "K"