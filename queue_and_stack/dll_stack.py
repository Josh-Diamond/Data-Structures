import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# Stack will ADD to the FRONT and remove from the FRONT
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size


# # Solution 1:
# list = [1, 2, 3]
# print(list[::-1])
#
# # Solution 2:
# list.reverse()
# print(list)