from src.annt import SoftAssert as Assert
#import runpy
@Assert
def hello():
    Assert.assertEquals(1,1)
    Assert.assertEquals(1,1)

@Assert
def hello2():
    Assert.assertEquals(5,81)
    Assert.assertEquals(11,112)
        
if __name__ == "__main__" :
    hello()
    hello2()
#    op=runpy.run_path("/Users/vaikuntj/Work/EclipseWS/MYexp/src/dec.py")
#    print op
#    print "Hi"