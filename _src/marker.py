import inspect,traceback
from _src.runner import TestRun
from _src.utilities import Utilities
from _src.annt import Verify
from _src.read_conf import ReadConfig
from _src.reporter import Reporter, TestReport

class Marker(object):
    def __init__(self, *arg_label):
        self.marker = arg_label
        
    def __call__(self, original_func):
        
        def _inner_func(*args, **kwargs):
            test_file_src_path = inspect.getsourcefile(original_func)
            if ReadConfig().marker in self.marker :
                    test_fixture_name = TestRun.get_class_name(test_file_src_path, ReadConfig().test_case_fixture_suffix)
                    fixture_import_handle = Utilities.get_fixture_from_path(test_file_src_path)
                    fixture_obj = getattr(fixture_import_handle, test_fixture_name)()
                    try:
                        getattr(fixture_obj, 'setup')()
                        sa = Verify()
                        sa.__call__(original_func)
                    except AssertionError :
                        Reporter.add_test_report(TestReport(original_func.__name__,"FAILED",[traceback.format_exc()],test_file_src_path))
                    except :
                        Reporter.add_test_report(TestReport(original_func.__name__,"Exception",[],test_file_src_path))
                    finally:
                        getattr(fixture_obj, 'teardown')()
            else:
                Reporter.add_test_report(TestReport(original_func.__name__,"SKIPPED",[],test_file_src_path))
        return _inner_func        
