#!/usr/bin/python
# -*- coding: utf-8 -*-

__create__ = '2017. 03. 02'
__author__ = 'mhbaek'

class Node:
    def __init__(self, _data, _next=None):
        self.data = _data
        self.next = _next


class LinkedList:
    def __init__(self, _node, _node_count=1):
        if _node:
            self.node = _node
            self.node_count = _node_count
        else:
            self.node = None
            self.node_count = 0

    def linked_list_size(self):
        return self.node_count

    def print_linked_list(self, debug=False):
        # print 'list count', self.node_count
        next_node = self.node

        print_string = ''
        # if self.node_count == 1:
        # print_string += str(next_node.data)

        while next_node:
            if next_node.next:
                if debug:
                    print self.node_count, next_node.data, next_node.next, '------->'
                print_string += str(next_node.data) + ' -------> '
            else:
                if debug:
                    print self.node_count, next_node.data, next_node.next
                print_string += str(next_node.data)
            next_node = next_node.next
        return print_string

    def add_node(self, _node):
        if self.node is None:
            self.node = _node
            self.node_count += 1
            return True

        next_node = self.node
        while next_node.next:
            next_node = next_node.next

        if next_node.next is None:
            next_node.next = _node
            self.node_count += 1
            return True

        return False

    def delete_node(self, _node):
        delete_node_data = _node.data
        previous_node = self.node
        next_node = self.node.next

        if previous_node.data == delete_node_data:
            del previous_node
            self.node = None
            self.node_count -= 1
            return True

        while next_node:
            if next_node.data == delete_node_data:
                previous_node.next = next_node.next
                del next_node
                self.node_count -= 1
                return True

            previous_node = next_node
            next_node = next_node.next

        return False
def linked_list_test():
    head_node = Node(1)
    linked_list = LinkedList(head_node)
    print 'list size', linked_list.linked_list_size()
    print linked_list.print_linked_list()
    node_1 = Node(2)
    node_2 = Node(3)
    node_3 = Node(4)
    node_4 = Node(6)
    print linked_list.add_node(node_1)
    print linked_list.add_node(node_2)
    print 'list size', linked_list.linked_list_size()
    print linked_list.add_node(node_3)
    print linked_list.add_node(node_4)
    print 'list size', linked_list.linked_list_size()

    print linked_list.print_linked_list(False)
    node_10 = Node(3)
    print linked_list.delete_node(node_10)
    print linked_list.print_linked_list(False)
    node_10 = Node(2)
    print linked_list.delete_node(node_10)
    print linked_list.print_linked_list(False)
    node_10 = Node(4)
    print linked_list.delete_node(node_10)
    print linked_list.print_linked_list(False)
    node_10 = Node(6)
    print linked_list.delete_node(node_10)
    print linked_list.print_linked_list(False)
    node_10 = Node(1)
    print linked_list.delete_node(node_10)
    print linked_list.print_linked_list(False)

    print'=============================================='
    print 'list size', linked_list.linked_list_size()
    print'=============================================='


    node_1 = Node(2)
    node_2 = Node(3)
    node_3 = Node(4)
    node_4 = Node(6)
    print linked_list.add_node(node_1)
    print linked_list.print_linked_list(False)
    print linked_list.add_node(node_2)
    print 'list size', linked_list.linked_list_size()
    print linked_list.print_linked_list(False)
    print linked_list.add_node(node_3)
    print linked_list.print_linked_list(False)
    print linked_list.add_node(node_4)
    print 'list size', linked_list.linked_list_size()
    print linked_list.print_linked_list(False)


if __name__ == '__main__':
    linked_list_test()
