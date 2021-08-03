# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_l1 = ''
        current = l1
        list_l1 += str(current.val)
        while current.next != None:
            current = current.next
            list_l1 += str(current.val)
        list_l2 = ''
        current = l2
        list_l2 += str(current.val)
        while current.next != None:
            current = current.next
            list_l2 += str(current.val)

        result = int(list_l1[::-1])+int(list_l2[::-1])
        node = None
        for idx, x in enumerate(str(result)):
            if idx == 0:
                node = ListNode(x)
                continue
            node = ListNode(x, node)

        return node
