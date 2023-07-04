class node:
    def __init__(self,data):
        self.data  = data
        self.ref = None
node1 = node(10)
print(node)
print("yes")

#create class for linking

class linkedlist:
    def __init__(self):
        self.head = None 
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n= self.head
           

    