import ConfigParser

class ReadConfig:
    
    config_file_path="conf/default.conf"
    def __init__(self):
        conf = ConfigParser.SafeConfigParser()
        if len(str(ReadConfig.config_file_path).strip())==0 :
            pass # Need to add an exception class  <Customized Exception classes>
        conf.read(ReadConfig.config_file_path)
        self.conf = conf

    def get(self, item_name, default_value=None):
        try:
            return self.conf.get("TEST_PARAM", item_name)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            return default_value
    
    @property
    def test_discovery_regex(self):
        """Regular Expression for test discovery"""
        return self.get("TEST_DISCOVERY_REGEX", "^^test_([a-z]|[A-Z]|[0-9])*$")

    @property
    def test_case_class_suffix(self):
        """Suffix for the class containing tests"""
        return self.get("TEST_CASE_CLASS_SUFFIX", "Tests")
    
    @property
    def test_case_fixture_suffix(self):
        """Suffix for the fixture class of the test class"""
        return self.get("TEST_CASE_FIXTURE_SUFFIX","Fixture")

    @property
    def marker(self):
        """Default marker for tests"""
        return self.get("MARKER",'T1')
   
    @property
    def ignore_file_name(self):
        """List of file names to be ignored"""
        return self.get("IGNORE_FILE_NAME",['__init__']) 
    
    @property
    def test_file_extension(self):
        """Extension of the test file """
        return self.get("TEST_FILE_EXTENSION",".py")
    
    @property
    def reference_dir_path(self):
        """Reference directory path for managing test imports"""
        return self.get("REFERENCE_DIR_PATH","/Users/vaikuntj/Work/Testing/JATR")
    
    @property
    def reserved_directories(self):
        """List of directories which are to ignored"""
        return self.get("RESERVED_DIRECTORIES",['.git','runner','_src','__pycache__'])