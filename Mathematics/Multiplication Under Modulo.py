 def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''   
        # code here
        res = (a*b)%(10**9+7)
        return res
