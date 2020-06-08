*****You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.


==>class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None
    def insert(self, val):
        if self.root==None:
            self.root=Node(val)
        else:
            cur=self.root 
            while True:
                if val<=cur.info:
                    if cur.left:
                        cur=cur.left
                    else:
                        cur.left=Node(val)
                        cur=cur.left
                        break
                elif val>cur.info:
                    if cur.right:
                        cur=cur.right
                    else:
                        cur.right=Node(val)
                        cur=cur.right
                        break
                else:
                    break
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)


LOGIC:-Compare the given value with the value of the nodes and accordingly move to the left or right of the node.