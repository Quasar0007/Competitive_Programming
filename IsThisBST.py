""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkBSTS(root, minv, maxv):
    if root == None :
        return True
    elif minv < root.data < maxv:
        return checkBSTS(root.left, minv, root.data) and checkBSTS(root.right, root.data, maxv)
    else:
        return False
    
        
def checkBST(root):
    return checkBSTS(root, float("-inf"), float("inf"))
        