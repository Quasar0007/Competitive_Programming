class Solution:
    def inorderTraversal(self, root, arr):
      
        if (root == None):
            return arr
      
        # first recur on left subtree
        self.inorderTraversal(root.left,arr)
      
        # then copy the data of the node
        arr.append(root.data)
      
        # now recur for right subtree
        self.inorderTraversal(root.right,arr)
        
        return arr
      
    def BSTToMaxHeap(self, root, arr):
      
        global i
        if (root == None):
            return None
      
        # recur on left subtree
        root.left = self.BSTToMaxHeap(root.left,arr)
      
        # recur on right subtree
        root.right = self.BSTToMaxHeap(root.right,arr)
      
        # copy data at index 'i' of 'arr' to
        # the node
        root.data = arr[i]
        i = i + 1
        return root
        
    # Utility function to convert the given BST to
    # MAX HEAP
    def convertToMaxHeapUtil(self, root):
        global i
          
        # vector to store the data of all the
        # nodes of the BST
        i = 0
        arr = []
      
        # inorder traversal to populate 'arr'
        arr = self.inorderTraversal(root,arr)
      
        # BST to MAX HEAP conversion
        root = self.BSTToMaxHeap(root,arr)
        
        return root