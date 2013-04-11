import types
from _src.reporter import Reporter, TestReport
import traceback,inspect

class DataMarker(object):
    def __init__(self, data_args):
        self.args = data_args
        
    def __call__(self, original_func):
        if isinstance(self.args,types.ListType)== True:
            self.f=original_func
            test_file_src_path = inspect.getsourcefile(original_func)
            try:
                for num in self.args:
                    getattr(self,'f')(self,num)
            except AssertionError :
                Reporter.add_test_report(TestReport(original_func.__name__,"FAILED",[traceback.format_exc()],test_file_src_path))
            except :
                Reporter.add_test_report(TestReport(original_func.__name__,"Exception",[],test_file_src_path))