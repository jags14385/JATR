class Param:
# under development  
    def __init__(self, *args):
        self.args = args
    
    def __call__(self, original_func):
            print original_func.__name__
            print original_func.func_globals['__name__']
            for arg in self.args:
                print arg
