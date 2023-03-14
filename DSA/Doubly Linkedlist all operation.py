
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linklist:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        a=Node(data)
        a.next=self.head
        if self.head is not None:
            self.head.prev=a
        self.head=a
    #Insert at first
    def insert_at_first(self,data):
        a=Node(data)
        a.next=self.head
        self.head=a
    #Insert at end
    def insert_at_end(self,data):
        a=Node(data)
        b=self.head
        while b.next is not None:
            b=b.next
        b.next=a
  
    def printlist(self):
        a=self.head
        while a is not None:
            print(a.data,end="->")
            a=a.next


p=linklist()

n=int(input("Enter your number of nodes:-"))

for i in range(0,n):
    q=int(input())
    p.push(q)

p.printlist()
p.insert_at_first(10)
print()
p.printlist()
print()
p.insert_at_end(900)
p.printlist()
