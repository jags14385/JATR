import copy
import json

class TestReport:
    def __init__(self, test_name, test_status, test_assertion_list,testfilepath):
        self.name = test_name
        self.status = test_status
        self.assertion_status_list = copy.deepcopy(test_assertion_list)
        self.testfilepath = testfilepath

class Reporter:
    test_report_list = []
    
    @classmethod
    def get_report_list(cls):
        return cls.test_report_list
    
    @classmethod
    def add_test_report(cls, test_report_instance):
        cls.test_report_list.append(test_report_instance)
    
    @classmethod    
    def num_tests_executed(cls):
        return len(cls.test_report_list)
    
    @classmethod
    def num_tests_passed(cls):
        test_pass_ctr = 0
        for test in cls.get_report_list():
            if test.status == 'PASS':
                test_pass_ctr += 1
        return test_pass_ctr
    
    @classmethod
    def num_tests_failed(cls):
        test_fail_ctr = 0
        for test in cls.get_report_list():
            if test.status == 'FAIL':
                test_fail_ctr += 1
        return test_fail_ctr
    
    @classmethod
    def test_results_display(cls):
        msg = ""
        for test in cls.get_report_list():
                print test.name + "[ " + test.status + " ]"
                if test.status == "FAIL":
                    for assertion in test.assertion_status_list:
                        msg_list = assertion.split(" ")
                        interim_msg = str(msg_list[1:])
                        msg = msg + interim_msg
                    if msg.strip() is not None and msg.strip() != "":
                        print "Assertions failed for : " + test.name + "\n" + msg
    @classmethod
    def json_repr(cls):
        json_list=[]
        for test_report in  cls.get_report_list():
            json_list.append(test_report.__dict__)
                
        json_report = {"TEST_EXECUTION_REPORT":json_list}
        return json.dumps(json_report)
