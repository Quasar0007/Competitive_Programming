class Solution:
    def findIntersection(self, head1, head2):
        d={}
        llist=linkedList()
        cur2=head2
        while cur2.next!=None:
            cur2=cur2.next
        cur2.next=head1
        cur1 = head2
        while cur1!=None:
            if cur1.data in d.keys():
                llist.insert(cur1.data)
            else:
                d[cur1.data]=1
            cur1=cur1.next
        return llist.head