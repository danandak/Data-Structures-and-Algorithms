# Tugas SDA 2 (Nomor 4) - Membuat Linked List
# Versi 1 (buat kelas dan fungsi sendiri)

# Untuk bikin linked list
import LinkedList

# Untuk bikin tulisan berwarna
from colorama import Fore, init, Style
init(autoreset = True)

linkedlist = LinkedList.linked_list()
pilihan = None

print("\n-------- SELAMAT DATANG DI PROGRAM SIMULASI LINKED LIST -------")
LinkedList.menu()
while pilihan != 7:
	try:
		pilihan = int(input("\nMasukkan pilihan : "))
	except ValueError:
		print(f"{Fore.RED}Masukkan angka 1 - 7 untuk memilih menu")
	else:
		if pilihan == 1:
			linkedlist.add_last()

		elif pilihan == 2:
			linkedlist.add_beg()

		elif pilihan == 3:
			linkedlist.print_list()

		elif pilihan == 4:
			if linkedlist.head is None:
				print(f"{Fore.RED}Linked list kosong")
			else:
				data = input("Masukkan data yang akan dicari : ")
				linkedlist.find_node(data)
			LinkedList.menu()

		elif pilihan == 5:
			linkedlist.delete_node()

		elif pilihan == 6:
			if linkedlist.head is None:
				print(f"{Fore.RED}Linked list sudah kosong")
			else:
				linkedlist.DELETE()
				print(f"{Fore.GREEN}Linked list berhasil dikosongkan")
			LinkedList.menu()

		elif pilihan == 7:
			print("Terima kasih sudah menggunakan program ini !")
			exit()

		else:
			print(f"{Fore.RED}Masukkan angka 1 - 7 untuk memilih menu")