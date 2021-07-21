class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return 1+max(self.height(root.left), self.height(root.right))