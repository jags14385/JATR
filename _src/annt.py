assertion_status = []

class Verify:
    
    def __init__(self):
        pass
        
    def __call__(self, original_func):
        self.test_name = original_func.__name__
        self.f = original_func
        self.f(self)
        self.parseAssertions()
        verif_errs_list = globals().get('assertion_status')
        del verif_errs_list[:]
        
    @classmethod   
    def verifyEquals(cls, expected, actual):
        msg = ""
        if expected == actual:
            msg = "Status:True Expected:" + str(expected) + " Actual:" + str(actual)
        else:
            msg = "Status:False Expected:" + str(expected) + " Actual:" + str(actual)
        globals().get('assertion_status').append(msg)
                    
    def parseAssertions(self):
        assertion_status_list = globals().get('assertion_status')
        msg = ""
        if assertion_status_list is not None:
            for assertion in assertion_status_list:
                msg_list = assertion.split(" ")
                result = msg_list[0].strip()
                if result == "Status:False":
                    interim_msg = str(msg_list[1:])
                    msg = msg + interim_msg
            if msg.strip() is not None and msg.strip() != "":
                print "TESTCASE:" + self.test_name + " FAILED"
                print "TEST STATUS MSG: " + msg
            else:
                
                print "TESTCASE:" + self.test_name + " PASSED"
                
