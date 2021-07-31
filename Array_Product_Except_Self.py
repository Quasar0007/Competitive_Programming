class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_last = 1
        ar=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            ar[i]=prod_last
            prod_last*=nums[i]
        prod_first=1
        for j in range(len(nums)):
            ar[j]*=prod_first
            prod_first*=nums[j]
        return ar