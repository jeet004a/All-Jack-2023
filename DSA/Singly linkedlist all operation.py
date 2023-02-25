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

a=head()
a.head=Node(10)
b=Node(20)
c=Node(30)

a.head.next=b
b.next=c
a.printlist()