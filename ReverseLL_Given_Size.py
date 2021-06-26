class Solution:
    def reverse(self,head, k):
        if head==None:
            return
        else:
            stack=[]
            curr = head
            prev = None
            while curr != None:
                val = 0 
                while val<k and curr != None:
                    val+=1
                    stack.append(curr)
                    curr=curr.next
                while stack!=[]:
                    if prev is None:
                        prev = stack.pop()
                        self.head = prev
                    else:
                        prev.next = stack.pop()
                        prev = prev.next
        prev.next = None
        return self.head

        