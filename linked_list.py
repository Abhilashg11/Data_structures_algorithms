class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.ref

#Adding at the beggining
    def add_beg(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

#Adding at the end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

 #Adding in the middle(after)
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            print("ds")
            if x == n.data:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node             
            n = n.ref 

# #adding in the middle(before)
#     def add_before(self,data,x):
#         n = self.head
#         new_node = Node(data)
#         while n is not None:
#             if x == n.data:
#                 new_node.ref = self.head

                                
            

ll1 = LinkedList()
ll1.add_beg(100)
ll1.add_end(79)
ll1.add_end(10)
ll1.add_end(24)
ll1.add_beg(69)
# ll1.add_beg(39)
ll1.add_after(1623,69)
ll1.print_LL()



    


   
	    
	    
	        		


    
