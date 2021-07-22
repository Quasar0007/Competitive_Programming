class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        d={}
        cur=head
        while cur!=None:
            if cur.data==-1:
                return True
            else:
                cur.data = -1
                cur=cur.next
        return False