class Node:
	def __init__(self, data):
		self.link = None
		self.info = data
class LinkedList:
	def __init__(self):
		self.start = None
	def display_list(self):
		if self.start is None:
			print("The list is empty")
		p =self.start
		while p is not None:
			print(p.info, " ", end = " ")
			p = p.link
		print()
	def insert_at_end(self,data):
		temp = Node(data)
		if self.start is None:
			self.start = temp
			return
		p = self.start 
		while p.link is not None:
			p = p.link
		p.link = temp
	def create_list(self):
		n = int(input("Enter the number of node"))
		if n == 0:
			return
		for i in range(n):
			data = int(input("enter the number"))
			self.insert_at_end(data)
	def reverse_list(self):
		prev = None
		p = self.start
		while p is not None:
			next = p.link
			p.link = prev
			prev = p
			p = next
		self.start = prev
	def Bubble_sort_exdata (self):
		end = None
		while end != self.start.link:
			p = self.start 
			while p.link != end:
				q = p.link
				if p.info > q.info:
					p.info,q.info = q.info,p.info
				p = p.link
			end = p
	def Bubble_sort_exlink (self):
		end = None
		while end != self.start.link:
			r = p = self.start 
			while p.link != end:
				q = p.link
				if p.info > q.info:
					p.link = q.link
					q.link = p
					if p!= self.start:
						r.link = q
					else:
						self.start = q
					p,q =q,p
				r = p
				p = p.link
			end = p







list = LinkedList()
list.create_list()
list.display_list()
#list.reverse_list()
list.Bubble_sort_exlink()
list.display_list()






		