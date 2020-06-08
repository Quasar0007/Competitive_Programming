*****Complete the preOrder function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.


==>class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def preOrder(root):
    print(root.info,end=" ")
    if root.left and root.right is not None:
        preOrder(root.left)
        preOrder(root.right)
    elif root.left is not None:
        preOrder(root.left)
    elif root.right is not None:
        preOrder(root.right)
    else:
        return


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)


LOGIC:-Use recursion for the left and right sub-tree of any node to return their details and use "end" in the print statement to print the output result in space-separated lines.