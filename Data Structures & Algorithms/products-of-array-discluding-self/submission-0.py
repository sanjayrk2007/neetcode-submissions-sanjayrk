class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zcount=0
        zindex=0
        res=[0]*len(nums)
        for i in range(len(nums)):
            if(nums[i]!=0):
                product=product*nums[i]
            else:
                zcount+=1
                zindex=i
        if zcount>1:return [0]*len(nums)
        for i,c in enumerate(nums):
            if(zcount):res[i]=0 if c else product
            else:res[i]=product//c
            
        return res
        