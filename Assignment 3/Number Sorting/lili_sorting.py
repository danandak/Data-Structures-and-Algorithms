# Untuk linked list sorting

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None
		self.last = None

	def insert_and_sort(self, data):
		if self.head is None:
			self.head = Node(data)
			self.last = self.head
		else:
			masukan = Node(data)
			if masukan.data >= self.last.data:
				self.last.next = masukan
				self.last = masukan
			else:
				temp = self.head
				while temp is not None:
					if temp == self.head:
						if masukan.data <= temp.data:
							masukan.next = self.head
							self.head = masukan
							break
						elif masukan.data < temp.next.data:
							masukan.next = temp.next
							temp.next = masukan
							break
					else:
						if masukan.data >= temp.data and masukan.data < temp.next.data:
							masukan.next = temp.next
							temp.next = masukan
							break
					temp = temp.next

	def delete_data(self, data):
		temp = Node(None)
		deleted = False
		temp.next = self.head
		while temp.next is not None:
			if temp.next.data == data:
				if temp.next == self.head:
					self.head = temp.next.next
					deleted = True
					break
				elif temp.next == self.last:
					self.last = temp
					temp.next = None
					deleted = True
					break
				else:
					temp.next = temp.next.next
					deleted = True
					break
			else:
				temp = temp.next
		return deleted

	def print(self):
		jumlah = 0
		temp = self.head
		if temp is not None:
			while temp is not None:
				if temp.next is not None:
					print(temp.data, end=" -> ")
				else:
					print(temp.data)
				temp = temp.next
				jumlah += 1
			print(f"\nJumlah elemen = {jumlah}")
		else:
			print("**Linked list kosong**")
		menu()

	def DELETE(self):
		temp = self.head
		while temp is not None:
			temp = temp.next
			del self.head
			self.head = temp

def menu():
	print("\n^^^ Pilihan Menu ^^^")
	print("1. Masukkan data (satu per satu)")
	print("2. Masukkan data (Jumlah banyak)")
	print("3. Print data")
	print("4. Hapus data")
	print("5. Kosongkan linked list")
	print("6. Keluar")