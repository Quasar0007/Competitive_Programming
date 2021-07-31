class Node: 
    def __init__(self,val): 
        self.val = val 
        self.left = None
        self.right = None

        # denotes number of times (frequency) 
        # an element has occurred. 
        self.elecount = 1

        # denotes the number of nodes on left 
        # side of the node encountered so far. 
        self.lcount = 0
        
class Tree: 
    def __init__(self,root): 
        self.root = root 
    def insert(self,node): 

        """This function helps to place an element at 
            its correct position in the BST and returns 
            the count of elements which are smaller than 
            the elements which are already inserted into the BST. 
        """
        curr = self.root 
        cnt = 0
        while curr!=None: 
            prev = curr 
            if node.val>curr.val: 

                # This step computes the number of elements 
                # which are less than the current Node. 
                cnt += (curr.elecount+curr.lcount) 
                curr=curr.right 
            elif node.val<curr.val: 
                curr.lcount+=1
                curr=curr.left 
            else: 
                prev=curr 
                prev.elecount+=1
                break
        if prev.val>node.val: 
            prev.left = node 
        elif prev.val<node.val: 
            prev.right = node 
        else: 
            return cnt+prev.lcount 
        return cnt 
        
class Solution:
	def constructLowerArray(self,arr, n):
	    t = Tree(Node(arr[-1])) 
        ans = [0] 
        for i in range(n-2,-1,-1): 
            ans.append(t.insert(Node(arr[i]))) 
        return reversed(ans)