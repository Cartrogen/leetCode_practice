class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, node):
        if self.head is None:
            self.head = node
            return
        node.next_node = self.head
        self.head = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def insert_position(self, position, node):
        i = 1
        current_node = self.head
        while current_node.next_node is not None:
            if i == position - 1:
                temp_var = current_node.next_node
                current_node.next_node = node
                node.next_node = temp_var
                return
            current_node = current_node.next_node
            i += 1

    def delete_head(self):
        if self.head is None:
            print("No head to delete")
        self.head = self.head.next_node

    def delete_tail(self):
        if self.head is None:
            print("No head to delete")
        current_node = self.head
        while current_node.next_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = None

    def delete_position(self, position):
        if self.head is None:
            print("linked list does not exist")
        if position == 1:
            self.delete_head()
            return
        i = 1
        current_node = self.head
        while current_node.next_node is not None:
            if i == position - 1:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node
            i += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "-->")
            current_node = current_node.next_node
        print("End")
