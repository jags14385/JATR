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
        pattern = re.compile("^test_*")
        methodList=Utilities.get_method_names_from_obj(var_object)
        
        for method in methodList:
            print pattern.search(method).group(0)
    
    @classmethod
    def discover_files(cls):
        pass