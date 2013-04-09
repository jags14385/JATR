class Param(object):
    
    def __init__(self,args):
        self.data_params=args
    
    def __call__(self, original_func):
        for data_param in self.data_params:
#            original_func(data_param)
            print data_param