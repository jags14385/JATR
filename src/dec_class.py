from annt import SoftAssert as Assert

class AssertFixture:
    a = 3
    
    @classmethod
    def setUp(cls):
        print "Setup method Test Level /Method Level"
        
    @classmethod
    def setUp_class(cls):
        print "Setup method Class Level"
        
    @classmethod
    def tearDown(cls):
        print "TearDown method Test Level /Method Level"
        
    @classmethod
    def tearDown_class(cls):
        print "TearDown method Class Level"    
        
class AssertTests:           
    @Assert    
    def test_hello(self):
        Assert.assertEquals(11, 1)
        Assert.assertEquals(11, 11)
        Assert.assertEquals(AssertFixture.a, 2)
  
    @Assert 
    def test_try(self):
        print "Hello successfully run"    
        
    def run(self):
        self.test_hello()  
                  
