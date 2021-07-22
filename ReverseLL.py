class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        cur = head
        prev = None
        while cur.next != None:
            nxt=cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur.next = prev
        return cur