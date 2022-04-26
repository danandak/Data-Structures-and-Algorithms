# Untuk main_f.py

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class stack_lili:
	def __init__(self):
		self.head = None
		self.last = None
		self.len = 0
		
	def push(self, data): # Masukkan data di puncak stack
		new = Node(data)
		if self.head is None:
			self.head = new
			self.last = self.head
		else:
			new.next = self.head
			self.head = new
		self.len += 1

	def pop(self): # Keluarkan data teratas pada stack 
		nilai_pop = self.head.data
		self.head = self.head.next
		self.len -= 1
		return nilai_pop
	
	def get_top(self): 
		return str(self.head.data)

	def printN(self): 
		temp = self.head
		while temp is not None:
			print(temp.data, end='')
			temp = temp.next

	def printR(self):
		string = ""
		temp = self.head
		while temp:
			string += temp.data
			temp = temp.next
		for x in reversed(string):
			print(x, end="")
		print()