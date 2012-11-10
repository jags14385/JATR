import re
class Utilities:
    
    @classmethod
    def get_method_names_from_obj(cls,var_object):
        """
        This method allows to get all the function/method names from an given object
        """
#        methodList = [method for method in dir(object) if callable(getattr(object, method))]
        methodList=[]   
        for func in dir(var_object):
            if callable(getattr(var_object,func)):
                methodList.append(func)            
        return methodList
    
    @classmethod
    def get_test_case_names(cls,var_object):
        """
        This method allows to get all the test case names from an Test Class
        """
        regex="^^test_([a-z]|[0-9])*$"
        methodList=Utilities.get_method_names_from_obj(var_object)
        testCaseList=[]
        for method in methodList:
            matchObj= re.match(regex,method)
            if matchObj is not None:
                testCaseList.append(matchObj.group(0))
        return  testCaseList
    
    @classmethod
    def runTests(cls,var_object):
        test_case_list=Utilities.get_test_case_names(var_object)
        for test_case in test_case_list:
            getattr(var_object,test_case)()
    @classmethod
    def discover_files(cls):
        pass