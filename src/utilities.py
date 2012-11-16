import re
import inspect
import os
from src.constants import Constants
class Utilities:
    
    @classmethod
    def get_method_names_from_obj(cls, var_object):
        """
            This method allows to get all the function/method names from an given object
        """
#        methodList = [method for method in dir(object) if callable(getattr(object, method))]
        methodList = []   
        for func in dir(var_object):
            if callable(getattr(var_object, func)):
                methodList.append(func)            
        return methodList
    
    @classmethod
    def get_test_case_names(cls, var_object):
        """
            This method allows to get all the test case names from an Test Class
        """
        regex = Constants.TEST_DISCOVERY_REGEX
        methodList = Utilities.get_method_names_from_obj(var_object)
        testCaseList = []
        for method in methodList:
            matchObj = re.match(regex, method)
            if matchObj is not None:
                testCaseList.append(matchObj.group(0))
        return  testCaseList
    
    @classmethod
    def getFixture(cls, var_object):
#        To get the class name
        test_class_handle = var_object.__class__
        point_position = str(test_class_handle).rfind(".") + 1
        testcase = str(test_class_handle)[point_position:len(str(test_class_handle))]
        common_name_pos = testcase.find(Constants.TEST_CASE_CLASS_SUFFIX)
        test_fixture_name = testcase[0:common_name_pos] + Constants.TEST_CASE_FIXTURE_SUFFIX
        
#        Inorder to get the module Name <NEED TO BE REFACTORED>
        test_file_path = inspect.getsourcefile(test_class_handle)
        test_path_list = test_file_path.split(os.sep)
        refList = Constants.REFERENCE_DIR_PATH.split(os.sep)
        final_referenced_list = []
        for each_path in test_path_list:
            if each_path is test_path_list[len(test_path_list) - 1]:
                final_referenced_list.append(each_path.split(".")[0])
                continue
            if each_path not in refList:
                final_referenced_list.append(each_path)
        if len(final_referenced_list) == 1 :
            fixture_import_handle = __import__(".".join(final_referenced_list[:]))
        else:
            fixture_import_handle = __import__(".".join(final_referenced_list[:]))
        
        for element in final_referenced_list[1:len(final_referenced_list)]:    
            module_handle = getattr(fixture_import_handle,element) 
            fixture_import_handle=module_handle
        return getattr(fixture_import_handle, test_fixture_name)
    
    @classmethod
    def runTests(cls, var_object):
        test_case_list = Utilities.get_test_case_names(var_object)
        fixture_obj = Utilities.getFixture(var_object)()
        getattr(fixture_obj, 'setUp_class')()
        for test_case in test_case_list:
            getattr(fixture_obj, 'setUp')()
            getattr(var_object, test_case)()
            getattr(fixture_obj, 'tearDown')()
        getattr(fixture_obj, 'tearDown_class')()
