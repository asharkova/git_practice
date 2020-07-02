from UdacityAlgorithms.LinkedList import LinkedList, Element


def reverseList(head):
    if head is None or head.next is None:
        return head
    else:
        p = reverseList(head=head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)

    print(reverseList(ll.head))