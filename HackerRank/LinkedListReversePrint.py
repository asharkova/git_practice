#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    all_elements = []
    current = head
    while current:
        all_elements.append(str(current.data))
        current = current.next
    return '\n'.join(reversed(all_elements))


if __name__ == '__main__':
    llist = SinglyLinkedList()
    list = [10, 11, 15, 17, 20, 25, 26]
    for i in range(len(list)):
        llist_item = list[i]
        llist.insert_node(llist_item)
    print(reversePrint(llist.head))
