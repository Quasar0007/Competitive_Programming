class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        while curr_node!=None:
            nxt = curr_node.next
            if nxt==None:
                curr_node = None
                break
            elif nxt.next==None:
                curr_node.data=nxt.data
                curr_node.next=None
                break
            else:
                curr_node.data=nxt.data
                curr_node = nxt