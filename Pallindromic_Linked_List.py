class Solution:
    def isPalindrome(self, head):
        cur=head
        length=1
        while cur.next!=None:
            cur=cur.next
            length+=1
        x=length//2+length%2
        cur=head
        while x>0:
            x-=1
            prev=cur
            cur=cur.next
        pre=None
        while cur!=None:
            nxt=cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        prev.next = pre
        # print(prev.data,pre.data)
        init = head
        x=length//2+length%2
        cur=head
        # print(x)
        while x>0:
            cur=cur.next
            x-=1
        # print(cur.data)
        while cur!=None:
            if init.data!=cur.data:
                return 0
            else:
                init=init.next
                cur=cur.next
        return 1