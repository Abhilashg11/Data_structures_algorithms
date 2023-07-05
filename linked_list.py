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
# adding node
    def append(self,data):
        new_node = node(data) 
        cur = self.head    
        while cur.ref != None:
           cur = cur.ref
        cur.ref = new_node

# finding length
    def length(self):
        cur = self.head
        total = 0 
        while cur.ref!= None:
            total+=1
            cur = cur.ref
        return total    

    def display(self):
        elems = []
        cur_node = self.head
        while  cur_node !=None:
            cur_node = cur_node.ref
            elems.append(cur_node.data)
        print(elems)    

my_list = linkedlist()

my_list.display

my_list.append(1)
my_list.append(2)

my_list.display()



    