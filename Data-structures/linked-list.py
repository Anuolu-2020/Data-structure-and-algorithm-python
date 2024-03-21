class ListNode:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Add a new node to the linked list
    def add(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.length += 1
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        return
    # remove a node from the linked list
    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.value == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        self.length -= 1

    def list_length(self):
        return f"The length of the list is: {self.length}"


# Create a linked ListNode
linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(4)
linked_list.remove(1)
linked_list.add(3)
linked_list.add(5)

# Print the linked list
print(linked_list.print_list())
# Print the length of the linked list
print(linked_list.list_length())
