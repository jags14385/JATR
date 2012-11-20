from _src.constants import Constants
from _src.annt import SoftAssert

class Marker(object):
    def __init__(self,marker_label='T1'):
        self.marker = marker_label
        
    def __call__(self, original_func):
        def _inner_func(*args,**kwargs):
            if self.marker==Constants.MARKER:
                sa = SoftAssert()
                sa.__call__(original_func)
            else:
                pass
        return _inner_func        