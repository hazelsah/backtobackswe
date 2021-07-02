class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val


