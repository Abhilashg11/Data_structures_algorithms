class node:
    def __init__(self,data=None):
        self.data  = data
        self.ref = None
# node1 = node(10)
# print(node1)


#create class for linking

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data) 
        cur = self.head    
        while cur.ref != None:
           cur = cur.ref
        cur.ref = new_node
        
    def length(self):
        cur = self.head
        total = 0 



    