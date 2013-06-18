from _src.read_conf import ReadConfig

class DataDriven(object):
    def __init__(self, marker=ReadConfig().marker,args=None):
        if args is None:
            raise Exception,"NO data arguments present"
        self.args = args
        self.marker=marker
        
    def __call__(self, original_func):
        
        def _inner_func(*args, **kwargs):
            pass
        return _inner_func
