import os
from _src.constants import Constants

def get_directories(path):
    discovered_directories=[]
    for component in os.listdir(path):
        if os.path.isdir(Constants.REFERENCE_DIR_PATH+os.sep+component) and component not in Constants.RESERVED_DIRECTORIES:
            discovered_directories.append(component)
    return discovered_directories


if __name__ == "__main__" :
    
    print get_directories(Constants.REFERENCE_DIR_PATH)
    
#        if os.path.isdir(component):
#            print os.path.dirname(component)
#        if component not in Constants.RESERVED_DIRECTORIES:
#            abs_path=Constants.REFERENCE_DIR_PATH+os.sep+component
#            if os.path.isdir(abs_path):
#                discovered_directories.append(component)
#    print discovered_directories     
#    for path,directory,files in os.walk(Constants.REFERENCE_DIR_PATH):
#        print directory
#        for directory in discovered_directories:
#            for name in files:
#                if fnmatch(name, Constants.PATTERN):
#                    print os.path.join(path, name)