import os
from _src.constants import Constants
import tokenize
from _src.utilities import Utilities

class TestRun:
    
    @classmethod
    def get_directories(cls,path):
        discovered_directories = []
        for component in os.listdir(path):
            if os.path.isdir(Constants.REFERENCE_DIR_PATH + os.sep + component) and component not in Constants.RESERVED_DIRECTORIES:
                discovered_directories.append(component)
        return discovered_directories

    @classmethod
    def get_class_name(cls,file_path,suffix):
        with open(file_path) as file_obj:
            tokens = tokenize.generate_tokens(file_obj.readline)
            for _, token, _, _, source_line in tokens:
                if token == 'class':
                    class_name_token = source_line.strip().split(' ')[1]
                    common_name_pos = class_name_token.find(suffix)
                    if common_name_pos >= 0:
                        class_name=class_name_token[:common_name_pos] + suffix
            file_obj.close()
        return class_name

    @classmethod
    def get_test_class(cls,test_path,file_name,test_class_name):
        test_path_list=test_path.split(os.sep)
        ref_list = Constants.REFERENCE_DIR_PATH.split(os.sep)
        final_referenced_list=[]
    
        for each_path in test_path_list:
            if each_path not in  ref_list:
                final_referenced_list.append(each_path)
        final_referenced_list.append(file_name)
        import_stmt=".".join(final_referenced_list)
        import_handle=__import__(import_stmt)        
   
        for each_import in final_referenced_list[1:len(final_referenced_list)]:
            import_handle=getattr(import_handle,each_import)
        test_class_import_reference=getattr(import_handle,test_class_name)
        return test_class_import_reference

    @classmethod    
    def executeTestRun(cls):    
        for directory in cls.get_directories(Constants.REFERENCE_DIR_PATH):
            for r, _, test_files in os.walk(Constants.REFERENCE_DIR_PATH + os.sep + directory):
                for test_file in test_files:
                    file_name, file_extension = os.path.splitext(test_file)
                    if file_extension in Constants.TEST_FILE_EXTENSION and file_name not in Constants.IGNORE_FILE_NAME:
                        test_class_name = cls.get_class_name(r + os.sep + test_file,Constants.TEST_CASE_CLASS_SUFFIX)
                        test_class_instance=cls.get_test_class(r, file_name, test_class_name)()
                        Utilities.runTests(test_class_instance)