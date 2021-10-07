from leet_code.linked_list import Node


def merge_k_lists(main_list):
    if len(main_list) == 0:
        return None
    
    while len(main_list) > 1:
        temp_merged_list = []
        for i in range(0, len(main_list), 2):
            l1_node = main_list[i]
            if i + 1:
                l2_node = main_list[i + 1]
            else:
                l2_node = None
            temp_merged_list.append(sort_linked_lists(l1_node, l2_node))
        main_list = temp_merged_list

    return main_list[0]


def sort_linked_lists(l1_node, l2_node):
    dummy_node = Node(None)
    current_node = dummy_node

    while l1_node and l2_node:
        if l1_node.data < l2_node.data:
            current_node.next_node = l1_node
            l1_node = l1_node.next_node
            current_node = current_node.next_node
        else:
            current_node.next_node = l2_node
            l2_node = l2_node.next_node
            current_node = current_node.next_node

    if l1_node:
        current_node.next_node = l1_node
    elif l2_node:
        current_node.next_node = l2_node

    return dummy_node.next_node
