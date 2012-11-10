import re
import inspect
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
        regex = "^^test_([a-z]|[0-9])*$"
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
        testcase= str(test_class_handle)[point_position:len(str(test_class_handle))]
        common_name_pos=testcase.find("Tests")
        testFixture = testcase[0:common_name_pos]+"Fixture"

#        Inorder to get the module Name
        src_file_path=inspect.getsourcefile(test_class_handle)
        fixture_module=inspect.getmodulename(src_file_path)
        module_import_handle=__import__(fixture_module)
        strk="module_import_handle."+testFixture
        objk=eval(strk)  
        return objk
    
    @classmethod
    def runTests(cls, var_object):
        test_case_list = Utilities.get_test_case_names(var_object)
        fixture_obj=Utilities.getFixture(var_object)()
        getattr(fixture_obj, 'setUp_class')()
        for test_case in test_case_list:
            getattr(fixture_obj, 'setUp')()
            getattr(var_object, test_case)()
            getattr(fixture_obj, 'tearDown')()
        getattr(fixture_obj, 'tearDown_class')()
    @classmethod
    def discover_files(cls):
        pass
