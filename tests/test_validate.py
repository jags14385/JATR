from _src.base_test_fixture import BaseTestFixture
from _src.annt import SoftAssert as Assert

class GMailFixture(BaseTestFixture): 
    @classmethod
    def setUp(cls):
        cls.a = 2
    
    @classmethod    
    def tearDown(cls):
        print "TearDown method Test Level /Method Level"

class GMailTests:
	 @Assert
	 def test_openURL(self):
		 Assert.assertEquals(GMailFixture.a, 1)