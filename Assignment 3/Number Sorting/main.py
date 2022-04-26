# Tugas 3 SDA (4) - Mengurutkan Data dengan Linked List
# Hanya menerima data berupa bilangan bulat
# Metode pengurutan data : kecil ke besar (ascending)

import lili_sorting

print("\n-------- SELAMAT DATANG DI PROGRAM MENGURUTKAN DATA DENGAN LINKED LIST -------")
LinkedList = lili_sorting.linked_list()
lili_sorting.menu()

pilihan = None
while pilihan != 6:
	try:
		pilihan = int(input("\nMasukkan pilihan : "))
	except:
		print("**Masukkan angka 1 - 6 untuk memilih menu**")
	else:
		if pilihan == 1:
			Error = True
			while Error is True:
				try:
					data = int(input("Masukkan data : "))
				except:
					print("**Masukkan data berupa bilangan bulat**\n")
				else:
					Error = False
					LinkedList.insert_and_sort(data)
					print(f"**Data '{data}' berhasil dimasukkan**")
					lili_sorting.menu()

		elif pilihan == 2:
			print("Masukkan data berupa angka (pisahkan data dengan spasi) :")
			data = [int(y) for y in input().split()]

			for x in data:
				LinkedList.insert_and_sort(x)
			print("**Data berhasil dimasukkan**")

			lili_sorting.menu()

		elif pilihan == 3:
			LinkedList.print()

		elif pilihan == 4:
			if LinkedList.head is None:
				print("**Linked list kosong**")
			else:
				Error = True
				while Error is True:
					try:
						data = int(input("Masukkan data yang ingin dihapus (bilangan bulat) : "))
					except:
						print("**Masukkan bilangan bulat**\n")
					else:
						Error = False
						if LinkedList.delete_data(data):
							print(f"**Data '{data}' berhasil dihapus**")
						else:
							print(f"**Data '{data}' tidak ditemukan**")
			lili_sorting.menu()

		elif pilihan == 5:
			if(LinkedList.head is None):
				print("**Linked list sudah kosong**")
			else:
				LinkedList.DELETE()
				print("**Linked list berhasil dikosongkan**")
			lili_sorting.menu()

		elif pilihan == 6:
			# print(f"self.last = {LinkedList.last.data}")
			print("Terima kasih telah menggunakan program ini !")
			exit()

		else:
			print("**Masukkan angka 1 - 6**")