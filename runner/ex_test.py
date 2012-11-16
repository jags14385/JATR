import os
from src.constants import Constants
from fnmatch import fnmatch

if __name__ == "__main__" :
    
    discovered_directories=[]
    for component in os.listdir(Constants.REFERENCE_DIR_PATH):
        if component not in Constants.RESERVED_DIRECTORIES:
            abs_path=Constants.REFERENCE_DIR_PATH+os.sep+component
            if os.path.isdir(abs_path):
                discovered_directories.append(component)
    print discovered_directories     
    for path,directory,files in os.walk(Constants.REFERENCE_DIR_PATH):
        print directory
        for directory in discovered_directories:
            for name in files:
                if fnmatch(name, Constants.PATTERN):
                    print os.path.join(path, name)