from UdacityAlgorithms.LinkedList import LinkedList, Element


class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head


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

    solution = Solution()
    print(solution.swapPairs(ll.head).value)
