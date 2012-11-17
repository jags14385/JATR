import os
from _src.constants import Constants
import tokenize

def get_directories(path):
    discovered_directories = []
    for component in os.listdir(path):
        if os.path.isdir(Constants.REFERENCE_DIR_PATH + os.sep + component) and component not in Constants.RESERVED_DIRECTORIES:
            discovered_directories.append(component)
    return discovered_directories

def get_class_name(token_str):
    with open(r + os.sep + test_file) as file_obj:
        tokens = tokenize.generate_tokens(file_obj.readline)
        for _, token, _, _,source_line in tokens:
            if token == 'class':
                class_name=source_line.strip().split(' ')[1]
                common_name_pos = class_name.find(Constants.TEST_CASE_CLASS_SUFFIX)
                if common_name_pos >= 0:
                    return class_name[:common_name_pos]+Constants.TEST_CASE_CLASS_SUFFIX
        file_obj.close()


if __name__ == "__main__" :
    
    for directory in get_directories(Constants.REFERENCE_DIR_PATH):
        for r, directories, test_files in os.walk(Constants.REFERENCE_DIR_PATH + os.sep + directory):
            for test_file in test_files:
                file_name, file_extension = os.path.splitext(test_file)
                if file_extension in Constants.TEST_FILE_EXTENSION and file_name not in Constants.IGNORE_FILE_NAME:
                    print get_class_name(r+os.sep+test_file)