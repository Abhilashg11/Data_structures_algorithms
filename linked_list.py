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
                print(n.data)
                n = n.ref
    def add(self,data):
        new_node = Node(data)
        new_node.ref = self.head
#         self.head = new_node


# ll1 = LinkedList()
# ll1.add(10)
# ll1.print_LL()


# # class node1:
# # 	def __init__(self,data):
# # 		self.data = data
# # 		self.next = None
# # class linked_list:
	
# #     def __init__(self):
# # 	    self.head=node1()

# #     def append(self,data):
# # 	    new_node = node1(data)
# # 	    cur = self.head
# # 	    while cur.next!=None:
# # 		    cur = cur.next
		    
a=2
b=3	    
	        
f{"sdgdsg",a-b}	    
	    
	    
	        		


    