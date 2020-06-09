# Given a reference to the head of a doubly-linked list and an integer,data, create a new DoublyLinkedListNode object having data value data and insert it into a sorted linked list while maintaining the sort.


#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
def sortedInsert(head, data):
    a=DoublyLinkedListNode(data)
    cur=head
    nxt=head.next
    if a.data<=head.data:
        a.next=head
        a.prev=None
        head=a
    else:
        pre=head
        while a.data>cur.data:
            if cur.next is not None:
                pre.next=cur
                cur.prev=pre
                pre=cur
                cur.next=a
                a.next=nxt
                a.prev=cur
                cur=nxt
                if nxt.next is not None:
                    nxt=nxt.next
            else:
                if a.data>cur.data:
                    cur.next=a
                    a.prev=cur
                    a.next=None
                    cur.prev=pre
                    pre.next=cur
                    break
                else:
                    break

    return head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()


# LOGIC:-Insert the node between the current node and next node if the data of given node is greater than the current node.