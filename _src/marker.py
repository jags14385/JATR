import inspect 
from _src.runner import TestRun
from _src.utilities import Utilities
from _src.annt import Verify
from _src.read_conf import TestRunConfig

class Marker(object):
    def __init__(self,marker_label="T1"):
        self.marker = marker_label
        
    def __call__(self, original_func):
        
        def _inner_func(*args,**kwargs):
            if str(self.marker)==TestRunConfig().marker :
#                try:
                    test_file_src_path= inspect.getsourcefile(original_func)
                    test_fixture_name=TestRun.get_class_name(test_file_src_path,TestRunConfig().test_case_fixture_suffix)
                    fixture_import_handle=Utilities.get_fixture_from_path(test_file_src_path)
                    fixture_obj =getattr(fixture_import_handle, test_fixture_name)()
                    getattr(fixture_obj, 'setup')()
                    sa = Verify()
                    sa.__call__(original_func)
#                except AssertionError :
#                    print "Assertion Error :("
#                finally:
                    getattr(fixture_obj, 'teardown')()
            else:
                pass
        return _inner_func        