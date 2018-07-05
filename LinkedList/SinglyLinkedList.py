# Implementation of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0
    
    def append(self,data):
        if self.root is None:
            self.root = Node(data)
            self.length += 1
        else:
            self._append(self.root, data)

    def _append(self, cur_node, data):
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = Node(data)
        self.length += 1
    
    def print_length(self):
        return self.length
    
    def print_LinkedList(self):
        if self.root is None:
            print("Linked list is empty")
        else:
            self._print_LinkedList(self.root)

    def _print_LinkedList(self, cur_node):
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

    def remove_elem(self, index):
        if index < 1 or index > self.print_length():
            print("Invalid index")
            return
        elif index == 1:
            self.root = self.root.next
            self.length -= 1
        else:
            count = 1
            cur_node  = self.root
            while count != index:
                count += 1
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = cur_node.next
            self.length -= 1
            del cur_node
            
LL = LinkedList()
LL.append(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.append(5)
LL.append(6)
LL.append(7)
LL.append(8)
LL.append(9)
LL.append(10)
# LL.print_LinkedList()
LL.remove_elem(1)
LL.print_LinkedList()
print("Length is: ", LL.print_length())