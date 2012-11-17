from _src.utilities import Utilities
from tests.dec import  AssertTests
#from tests.dec import AssertTests

if __name__ == "__main__" :
    t = AssertTests()
    Utilities.runTests(t)
    print "hi"
    