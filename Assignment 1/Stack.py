# SDA - Tugas Kelompok 1 (Kelompok 5)
# Membuat Stack dengan Limit Kapasitas 
# limit kapasitas ditentukan oleh user

# inisialisasi stack 
stack = []
kapasitas = None

# choose = 1
def Push():
    if len(stack) < kapasitas :
        insert = input("Masukkan elemen baru : ")
        stack.append(insert)
        print(f"**Elemen \"{insert}\" berhasil dimasukkan**")
    else:
        print("**Stack penuh, tidak dapat memasukkan elemen lagi**")
    menu()

# choose = 2
def Pop():
    if len(stack) > 0:
        print(f"** Elemen \"{stack[len(stack)-1]}\" berhasil dikeluarkan **")
        stack.pop()
    else:
        print("**Error, stack kosong**")
    menu()

# choose = 3
def Print_Stack():
    if len(stack) == 0:
        print("**Stack kosong, tidak ada elemen yang tersimpan**")
    else:
        x = 0
        while x < len(stack):
            if x == len(stack) - 1:
                print(stack[x])
            else:
                print(stack[x], end=" -> ")
            x += 1
    menu()

# choose = 4
def Clear_Stack():
    if len(stack) == 0:
        print("**Stack sudah kosong**")
    else:
        stack.clear()
        print("**Stack berhasil dikosongkan**")
    menu()

# tampilkan menu
def menu():
    print()
    print("^^^ Menu yang tersedia ^^^")
    print("1. Masukkan elemen baru")
    print("2. Keluarkan elemen")
    print("3. Tampilkan elemen - elemen dalam Stack")
    print("4. Hapus semua elemen")
    print("5. Keluar")
    print(f"Jumlah elemen dalam stack saat ini : {len(stack)} elemen")
    print(f"Kapasitas maksimum stack : {kapasitas} elemen")

# main program
print("\n------- SELAMAT DATANG DI PROGRAM SIMULASI STACK -------")

Error = True
while Error is True:
    try:    
        kapasitas = int(input("Masukkan kapasitas stack yang diinginkan : "))
    except:
        print("**Error, masukkan bilangan bulat untuk kapasitas stack**\n")
    else:
        if kapasitas <= 0:
            print("**Masukkan bilangan bulat yang lebih besar dari 0**\n")
        else:
            Error = False

choose = None
menu()

while choose != 5:
    try:
        choose = int(input("\nPilih menu yang tersedia : "))
    except:
        print("**Masukkan angka 1 - 5 untuk memilih menu**")
    else:
        if choose == 1:
        	Push()
        elif choose == 2:
        	Pop()
        elif choose == 3:
            Print_Stack()
        elif choose == 4:
            Clear_Stack()
        elif choose == 5:
            print("Terima kasih telah menggunakan program simulasi stack ini")
            exit()
        else:
            print("**Pilihan tidak ada di menu, coba lagi**")