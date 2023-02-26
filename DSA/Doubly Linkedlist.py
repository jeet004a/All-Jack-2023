
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
