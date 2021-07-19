# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def level(self, x, root):
        if x.val == root.val:
            return 0
        elif x.val<root.val:
            return 1+self.level(x,root.left)
        else:
            return 1+self.level(x,root.right)
    def ancestor(self, x, root):
        parent = root
        child = root
        while child != x:
            if x.val<parent.val:
                store = parent.left
                parent = child
                child = store
            else:
                store = parent.right
                parent = child
                child = store
        return parent
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p
        else:
            if self.level(p, root)>self.level(q, root):
                new = self.ancestor(p, root)
                return self.lowestCommonAncestor(root, new, q)
            elif self.level(p,root)<self.level(q,root):
                new = self.ancestor(q, root)
                return self.lowestCommonAncestor(root, p, new)
            else:
                new_one = self.ancestor(p,root)
                new_two = self.ancestor(q,root)
                return self.lowestCommonAncestor(root, new_one, new_two)
        