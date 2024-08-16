import math
class Solution:
	def quadraticRoots(self, a : int, b : int , c:int ) -> List[int]:
        # code here
        res=list()
        
        #will be finding discriminant
        d = math.pow(b,2)-(4*a*c)
        
        #roots are imaginary
        if(d<0):
            res.append(-1)
            return res
            
        #now roots are either real or equal
        fr = math.floor((-b + math.sqrt(d))//(2*a))
        sr = math.floor((-b - math.sqrt(d))//(2*a))
        
        #maximum root followed by the minimum root
        res.append(max(fr,sr))
        res.append(min(fr,sr))
        
        #return the result list
        return res
