from _src.comparator import _Comparator
from _src.reporter import Reporter, TestReport
assertion_status = []

class Verify:
    
    def __init__(self):
        pass
        
    def __call__(self, original_func):
        self.test_name = original_func.__name__
        self.f = original_func
        self.f(self)
        self._parseAssertions()
        verif_errs_list = globals().get('assertion_status')
        Reporter.add_test_report(TestReport(self.test_name,self.status,verif_errs_list))
        del verif_errs_list[:]
        
    @classmethod
    def _append_assertion_msg(self, status, expected, actual):
        msg = ""
        if status == True:
            msg = "Status:True Expected:" + str(expected) + " Actual:" + str(actual)
        else:
            msg = "Status:False Expected:" + str(expected) + " Actual:" + str(actual)
        globals().get('assertion_status').append(msg)
            
    @classmethod   
    def verifyEquals(cls, expected, actual):
        status=_Comparator._verify_equals(actual, expected)
        cls._append_assertion_msg(status, expected, actual)
    
    @classmethod        
    def verifyTrue(cls, actual):
        status=_Comparator._verify_bool_values(actual,True)
        cls._append_assertion_msg(status, 'TRUE', actual)
        
    @classmethod        
    def verifyFalse(cls, actual):
        status=_Comparator._verify_bool_values(actual,False)
        cls._append_assertion_msg(status, 'FALSE', actual)
                    
    def _parseAssertions(self):
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
                self.status='FAIL'
            else:
                self.status='PASS'