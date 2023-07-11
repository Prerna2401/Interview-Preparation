class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self, head = None):
        self.head = head
        
    def search(self, head, data, idx):
        if head.data == data:
            print(idx)
        else:
            if head.next:
                return self.search(head.next, data, idx+1)
            else:
                raise ValueError("Node not in linked list")
            
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")
        
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next
        print("\n")
        
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while(current):
            size += 1
            current = current.next
            
        return size
    
    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        
    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0
    
    def insert(self, pos, data):
        head = self.head
        if (pos < 0):
            print("Invalid position!")
            
        if (pos == 0):
            node = Node(data)
            node.next = self.head
            self.head = node
            
        else:
            
            while (pos > 0):
                pos -= 1
                if (pos == 0):
                    node = Node(data)
                    node.next = head.next
                    head.next = node
                    break
                
                head = head.next
                if head == None:
                    break
                
            if pos != 0:
                print("Position out of range")
                
    def delete(self, pos):
        if self.head == None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                break
            
        if temp is None:
            print('Invalid Position')
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
                
Mylist = LinkedList()

n = int(input('Enter the number of elements: '))

for i in range(n):
    pos = int(input('Enter the position of insertion: '))
    ele = int(input('Enter the element to be inserted: '))
    Mylist.insert(pos, ele)

""" Mylist.insert(1, 10)
Mylist.insert(2, 20)
Mylist.insert(3, 30)
Mylist.insert(4, 40)

Mylist.insert(3, 50) """

Mylist.print_list()

ele = int(input('Enter the position of deletion: '))
Mylist.delete(ele)
Mylist.print_list()

srch = int(input('Enter the element to be searched for: '))
print('Element found at index: ')
Mylist.search(Mylist.head, srch, 0)

if Mylist.detect_loop():
    print('Loop found')
else:
    print('No Loop')

print('Reverse of the linked list is: ')
Mylist.reverse()
Mylist.print_list()