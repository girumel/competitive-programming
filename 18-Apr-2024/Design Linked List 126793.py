# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if current is None:
                return -1
            current = current.next
        if current is None:
            return -1
        return current.val
            

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.head = Node(val, self.head)
        else:
            current = self.head
            for _ in range(index-1):
                if current is None:
                    return
                current = current.next
            if current is None:
                    return
            current.next = Node(val, current.next)

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            if current is None or current.next is None:
                return
            current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)