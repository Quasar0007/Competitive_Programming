# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def BSTDC(self, nums):
        if len(nums)==0:
            return
        if len(nums)==1:
            return TreeNode(nums[0])
        else:
            mid = len(nums)//2
            root = nums[mid]
            left = self.BSTDC(nums[:mid])
            right = self.BSTDC(nums[(mid+1):])
            return TreeNode(root, left, right)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.BSTDC(nums)