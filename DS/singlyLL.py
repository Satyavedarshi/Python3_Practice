
class llnode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_ll_len(self):
        len = 0
        trav_node = self.head
        while(trav_node):
            len += 1
            trav_node = trav_node.next
        return len

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
    def remove_by_key(self,val):
        trav_node = self.head
        if val == trav_node.data:
            self.head = trav_node.next
            return
        while(trav_node):
            if val == trav_node.next.data:
                trav_node.next = trav_node.next.next
                return
            trav_node = trav_node.next

    def remove_by_index(self,rem_index):
        prev_node = None
        ll_len = self.get_ll_len()
        trav_node = self.head
        for curr_index in range(0,ll_len):
            if curr_index == rem_index:
                if trav_node == self.head :
                    self.head = trav_node.next
                    return
                elif trav_node.next == None :
                    prev_node.next = None
                    return
                else:
                    prev_node.next =  trav_node.next
                    return
            prev_node = trav_node
            trav_node = trav_node.next
        return

    def delete_ll(self):
        self.head = None

    def search_by_key(self,head,key):
        if not head:
            print('Item not found')
        elif head.data== key:
            print('Key found..')
        else:
            self.search_by_key(head.next,key)

    def get_node_by_n(self,head,key):
        counter = 0
        if key >= self.get_ll_len():
            print('Nth node does not exist')
            return
        elif key == counter:
            print(head.data)
            return
        else:
            self.get_node_by_n(head.next,key-1)

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
L1.push(1)
L1.print_linkedList()
print()
L1.insert_after_node(L1.head.next.next.next,7)
L1.print_linkedList()
print()
L1.remove_by_key(7)
L1.print_linkedList()
print()
L1.remove_by_key(1)
L1.print_linkedList()
print()
print(L1.get_ll_len())
L1.print_linkedList()
print()
L1.remove_by_index(3)
L1.print_linkedList()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
print()
L1.remove_by_index(0)
L1.print_linkedList()
print()
L1.search_by_key(L1.head,6)
L1.get_node_by_n(L1.head,2)
print()
L1.push(1)
L1.print_linkedList()
print()
L1.push(3)
L1.print_linkedList()
print()
L1.push(5)
L1.print_linkedList()
print()
L1.print_linkedList()
print()


L1.get_node_by_n(L1.head,2)
print()
L1.get_node_by_n(L1.head,3)
