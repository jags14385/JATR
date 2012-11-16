from _src.annt import SoftAssert as Assert
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