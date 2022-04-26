from colorama import Fore, init, Style
init(autoreset = True)

# Kelas untuk membuat Node / simpul
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Kelas untuk membuat linked list (6 fungsi)
class linked_list:
	def __init__(self):
		self.head = None
		self.last = self.head

	# Masukkan data baru di awal linked list
	def add_beg(self):
		Error = True
		while Error is True:
			try:
				jumlah = int(input("Jumlah data yang akan dimasukkan : "))
			except ValueError:
				print(f"{Fore.RED}Hanya masukkan bilangan bulat\n")
			else:
				Error = False
				for x in range(jumlah):
					data = input(f"\nMasukkan data ke - {x+1} untuk disisipkan di awal linked list : ")
					if self.head is None:
						self.head = Node(data)
						self.last = self.head
					else:
						new = Node(data)
						new.next = self.head
						self.head = new
					print(f"{Fore.GREEN}Data '{data}' berhasil dimasukkan")
		menu()

	# Masukkan data baru di akhir linked list
	def add_last(self):
		Error = True
		while Error is True:
			try:
				jumlah = int(input("Jumlah data yang akan dimasukkan : "))
			except ValueError:
				print(f"{Fore.RED}Hanya masukkan bilangan bulat\n")
			else:
				Error = False
				for x in range(jumlah):
					data = input(f"\nMasukkan data ke - {x+1} untuk disisipkan di akhir linked list : ")
					if self.head is None:
						self.head = Node(data)
						self.last = self.head
					else:
						new = Node(data)
						self.last.next = new
						# while search.next is not None:
						# 	search = search.next
						# last_node.pointer = new
						self.last = new
					print(f"{Fore.GREEN}Data '{data}' berhasil dimasukkan")
		menu()

	# Tampilkan linked list
	def print_list(self):
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
			print(f"{Fore.RED}Linked list kosong")
		menu()

	# Cari data tertentu dalam linked list
	def find_node(self, data):
		temp = self.head
		index = 1
		found = False
		while temp is not None:
			# if temp.data.lower().strip() == data.lower().strip():
			if temp.data == data:
				found = True
				break
			else:
				temp = temp.next
				index += 1
		if found is True:
			# print(f"{Fore.GREEN}data '{temp.data.strip()}' ditemukan pada urutan ke - {index}")
			print(f"{Fore.GREEN}data '{temp.data}' ditemukan pada urutan ke - {index}")
		else:
			# print(f"{Fore.RED}data '{data.strip()}' tidak ditemukan")
			print(f"{Fore.RED}data '{data}' tidak ditemukan")
		return(found)

	# Menghapus Node atau data dalam linked list
	def delete_node(self):
		if self.head is None:
			print(f"{Fore.RED}Linked list kosong")
		else:
			data = input("Masukkan data yang ingin dihapus : ")
			if linked_list.find_node(self, data) is True:
				temp = self.head
				Found = False
				while temp is not None:
					# if temp.data.lower().strip() == data.lower().strip():
					if temp.data == data:
						self.head = temp.next
						found = True
						break
					# elif temp.next.data.lower().strip() == data.lower().strip():
					elif temp.next.data == data:
						if temp.next == self.last:
							self.last = temp
						temp.next = temp.next.next
						found = True
						break
					else:
						temp = temp.next
				if found is True:
					print(f"{Fore.GREEN}Data '{data}' berhasil dihapus")
				# else:
				# 	print(f"{Fore.RED}Data '{data}' tidak ditemukan")
		menu()

	def DELETE(self):
		temp = self.head
		while(temp is not None):
			temp = temp.next
			del self.head
			self.head = temp

# Fungsi untuk print menu
def menu():
	print("\n^^^ Pilihan Menu ^^^")
	print("1. Tambahkan data di akhir")
	print("2. Tambahkan data di awal")
	print("3. Print linked list")
	print("4. Cari data / elemen")
	print("5. Hapus data / elemen")
	print("6. Kosongkan linked list")
	print("7. Keluar")