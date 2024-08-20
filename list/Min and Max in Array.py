class Solution:
    def get_min_max(self, arr):
        mini=arr[0]
        maxi=arr[0]
        for i in range(1,len(arr)):
            if(arr[i]<=mini):
                mini=arr[i]
            elif(arr[i]>maxi):
                maxi=arr[i]

      #result list containing minimum and maximum element
        res=[]
        res.append(mini)
        res.append(maxi)
        return res
