class Solution:
    def mirror(self,root):
        if root!=None:
            c = root.right
            d = root.left
            root.left = c
            root.right = d
            self.mirror(root.left)
            self.mirror(root.right)