class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
n1 = node()
print(n1.data)

class linked_list:
	def __init__(self):
		self.head=node()
		self.wei=no

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems) 

my_list = linked_list()

my_list.display

my_list.append(1)
my_list.append(2)

my_list.display()



# class node1:
# 	def __init__(self,data):
# 		self.data = data
# 		self.ref = None

# class linked_list:
	
#     def __init__(self):
# 	    self.head=node1()

#     def app    
	    
	    
	    
	        		


    