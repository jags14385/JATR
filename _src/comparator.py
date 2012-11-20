class _Comparator:
    
    @classmethod
    def _verify_bool_values(cls,actual, expected):
        if True == actual:
            return  True
        else:
            return False
    
    @classmethod    
    def _verify_equals(cls,actual,expected):
        
        if isinstance(actual, (list,dict,int,float)) == isinstance(expected, (list,dict,int,float)):
            if expected == actual:
                return  True
            else:
                return  False
        