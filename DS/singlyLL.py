
class llnode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = llnode(val)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,prev_node,val):
        new_node = llnode(val)
        if prev_node is None:
            print('Gave Invalid Node')
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,val):
        new_node = llnode(val)
        if self.head is None:
            self.head = new_node
            return
        iter_nodes = self.head
        while(iter_nodes.next):
            iter_nodes = iter_nodes.next
        iter_nodes.next = new_node

    def print_linkedList(self):
        if self.head is None:
            print('Linked List is Empty...')
            return
        iter_nodes = self.head
        while(iter_nodes):
            print(iter_nodes.data,end='-->')
            iter_nodes = iter_nodes.next



L1 = LinkedList()
L1.print_linkedList()
print()
L1.append(1)
L1.print_linkedList()
print()
L1.append(2)
L1.print_linkedList()
print()
L1.append(3)
L1.print_linkedList()
print()
L1.push(4)
L1.print_linkedList()
print()
L1.push(5)
L1.print_linkedList()
print()
L1.push(6)
L1.print_linkedList()
print()
L1.insert_after_node(L1.head.next.next.next,7)
L1.print_linkedList()
