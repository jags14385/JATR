from src.annt import SoftAssert as Assert
class AssertFixture:
    a=3
class AssertTests:
                  
    @Assert    
    def test_hello(self):
        Assert.assertEquals(11,1)
        Assert.assertEquals(11,11)
        Assert.assertEquals(AssertFixture.a,2)
        
    def run(self):
        self.test_hello()  
            
        
if __name__ == "__main__" :
    t=AssertTests()
    t.run()
