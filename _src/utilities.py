import re
import inspect
import os
from _src.read_conf import TestRunConfig
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
        regex =TestRunConfig().test_discovery_regex
        methodList = Utilities.get_method_names_from_obj(var_object)
        testCaseList = []
        for method in methodList:
            matchObj = re.match(regex, method)
            if matchObj is not None:
                testCaseList.append(matchObj.group(0))
        return  testCaseList
    
    @classmethod
    def getFixture(cls, var_object):
#       To get the class name
        test_class_handle = var_object.__class__
        point_position = str(test_class_handle).rfind(".") + 1
        testcase = str(test_class_handle)[point_position:len(str(test_class_handle))]
        common_name_pos = testcase.find(TestRunConfig().test_case_class_suffix)
        test_fixture_name = testcase[0:common_name_pos] + TestRunConfig().test_case_fixture_suffix
        
#        Inorder to get the module Name <NEED TO BE REFACTORED>
        test_file_path = inspect.getsourcefile(test_class_handle)
        fixture_import_handle=cls.get_fixture_from_path(test_file_path)
        return getattr(fixture_import_handle, test_fixture_name)
    
    @classmethod
    def get_fixture_from_path(cls,test_file_path):
        test_path_list = test_file_path.split(os.sep)
        refList = TestRunConfig().reference_dir_path.split(os.sep)
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
        return fixture_import_handle
    
    
    @classmethod
    def runTests(cls, var_object):
        test_case_list = Utilities.get_test_case_names(var_object)
        fixture_obj = Utilities.getFixture(var_object)()
        getattr(fixture_obj, 'setup_class')()
        for test_case in test_case_list:
            getattr(var_object, test_case)()
        getattr(fixture_obj, 'teardown_class')()
