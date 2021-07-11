class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_elem = float('-inf')
        max_sum = float('-inf')
        for i in nums:
            max_elem += i
            # print(max_elem)
            max_elem= max(max_elem, i)
            # print(max_elem)
            max_sum = max(max_sum, max_elem)
            # print(max_sum, max_elem)
        return max_sum