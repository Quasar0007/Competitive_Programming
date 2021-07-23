def findIntersection(head1,head2):
    l=linkedList()
    cur1=head1
    cur2=head2
    while cur1!=None and cur2!=None:
        if cur1.data==cur2.data:
            l.insert(cur1.data)
            cur1=cur1.next
            cur2=cur2.next
            
        elif cur1.data < cur2.data:
            cur1=cur1.next
        else:
            cur2=cur2.next
    return l.head