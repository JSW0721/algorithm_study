class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node = Node(3)
print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    def get_node(self,index):
        cur = self.head
        cur_index = 0
        
        return

linked_list = LinkedList(5)
print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)
