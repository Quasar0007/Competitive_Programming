# You are given a pointer to the root of a binary tree. You need to print the level order traversal of this tree. In level order traversal, we visit the nodes level by level from left to right. You only have to complete the function. For example:

#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4  
# For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.


class Node:
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
def levelOrder(root):
    l=[root]
    while True:
        top=l[0]
        if top.left is not None:
            l.append(top.left)
        if top.right is not None:
            l.append(top.right)
        if l!=[]:
            print(top.info,end=" ")
            del(l[0])
        if l==[]:
            break
        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)

# LOGIC:-Keep storing the nodes from left to right in the queue and using the addresses of the nodes ;append in the queue the left and right chldren of that node and keep doing it.