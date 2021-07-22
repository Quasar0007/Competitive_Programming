def level(root,a,lev):
    if root==None:
        return 0
    if root.data==a:
        return lev
    lev+=1
    return level(root.left,a,lev)+level(root.right,a,lev)
    
def parent(root,a):
    if root!=None:
        if root.left!=None:
            if root.left.data==a:
                return root.data
        if root.right!=None:
            if root.right.data==a:
                return root.data
        return max(parent(root.left,a),parent(root.right,a))
            
    return -1
    
    
    
    
def isCousin(root, a, b):
    if root.data==a or root.data==b:
        return False
    
    if level(root,a,0)==level(root,b,0):
        if parent(root,a)!=parent(root,b):
            return True
        else:
            return False
    else:
        return False