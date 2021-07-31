class Solution:
    def inord(self, root, l):
        if root.left!=None:
            self.inord(root.left,l)
        l.append(root.data)
        if root.right!=None:
            self.inord(root.right,l)
        return l
    def InOrder(self,root):
        l=[]
        return self.inord(root,l)