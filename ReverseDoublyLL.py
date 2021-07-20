def reverseDLL(head):
    prev=None
    cur=head
    while cur.next!=None:
        nxt = cur.next
        cur.next = prev
        cur.prev = nxt
        prev = cur
        cur = nxt
    cur.next = prev
    return cur