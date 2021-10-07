class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node

    @staticmethod
    def print_list(node):
        current_node = node
        while current_node:
            print(current_node.data, "-->")
            current_node = current_node.next_node


class Solution:

    @staticmethod
    def add_two_number(l1, l2):
        dummy = Node()
        new_current_node = dummy
        print(dummy.next_node)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.data
            else:
                v1 = 0

            if l2:
                v2 = l2.data
            else:
                v2 = 0

            val = v1 + v2 + carry
            carry = val // 10
            value = val % 10
            new_current_node.next_node = Node(value)

            # updating pointers

            if l1:
                l1 = l1.next_node
            else:
                l1 = None

            if l2:
                l2 = l2.next_node
            else:
                l2 = None

            new_current_node = new_current_node.next_node
        return dummy.next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "-->")
            current_node = current_node.next_node
