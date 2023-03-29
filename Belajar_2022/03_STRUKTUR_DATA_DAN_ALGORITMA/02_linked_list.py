class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):

        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next

        return total

    def print(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            print(current_node.data, end=" ")
        print()


my_ll = LinkedList()
my_ll.append("Anas")
my_ll.append("Budi")
my_ll.print()
print(my_ll.length())
