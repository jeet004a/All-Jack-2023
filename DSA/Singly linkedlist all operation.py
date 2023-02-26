class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class head:
    def __init__(self):
        self.head=None

    def printlist(self):
        a=self.head
        while a is not None:
            print(a.data,end="->")
            a=a.next
    # Insert at end
    def atend(self,data):
        x=Node(data)
        if self.head is None:
            self.head=x
            return
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=x
    # Insert beginning
    def atfirst(self,data):
        p=Node(data)
        p.next=self.head
        self.head=p
    # Insert at Position
    def pos(self,data,p):
        a=Node(data)
        p=p-1
        s=self.head
        c=0
        while c!=p:
            s=s.next
            c=c+1
        a.next=s.next
        s.next=a
        

a=head()
a.head=Node(10)
b=Node(20)
c=Node(30)

a.head.next=b
b.next=c
a.printlist()
#Insert at end
print()
a.atend(90)

a.printlist()
# Insert at first
print()
a.atfirst(20)
a.printlist()
#insert at position
print()
a.pos(23,3)
a.printlist()