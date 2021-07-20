class Solution:
    def areMirror(self,root1,root2):
        if root1!=None and root2!=None:
            if root1.data == root2.data:
                if (root1.left==None and root1.right==None) and (root2.left==None and root2.right==None):
                    return root1.data==root2.data
                elif (root1.left==None and root2.right==None):
                    return self.areMirror(root1.right, root2.left)
                elif (root1.right == None and root2.left==None):
                    return self.areMirror(root1.left, root2.right)
                else:
                    return self.areMirror(root1.left, root2.right) and self.areMirror(root1.right, root2.left)
            else:
                return False
        else:
            return False