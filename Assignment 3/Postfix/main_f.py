# Tugas 3 SDA (6) - Konversi Ekspresi Infix ke Postfix
# Stack diimplementasikan dengan linked list

import postfix_f as pf

prioritas = {
	'(':1,')':1,
	'+':2,'-':2,
	'*':3,'/':3,'%':3,
	'^':4
}

print("\n-------- SELAMAT DATANG DI PROGRAM KONVERSI INFIX KE POSTFIX --------")
ulangi = 'y'

while ulangi.lower() == 'y':
	string = input("\nMasukkan ekspresi infix yang akan diproses :\n")
	string = string.strip()
	
	stack_operator = pf.stack_lili()
	stack_hasil = pf.stack_lili()
	key = prioritas.keys()

	for x in string:
		if x not in key:
			stack_hasil.push(x)

		elif x in key and stack_operator.len == 0:
			stack_operator.push(x)

		elif x in key and stack_operator.len > 0:
			if x == '(':
				stack_operator.push(x)
			elif x == ')':
				kondisi = True
				while kondisi:
					if stack_operator.head.data == '(':
						kondisi = False
						stack_operator.pop()
						break
					else:
						stack_hasil.push(stack_operator.pop())
			else:
				if stack_operator.head.data != '(':
					if prioritas[x] > prioritas[stack_operator.get_top()]:
						stack_operator.push(x)
					else:
						while stack_operator.len > 0:
							if prioritas[x] <= prioritas[stack_operator.get_top()]:
								stack_hasil.push(stack_operator.pop())
							else:
								break
						stack_operator.push(x)
				else:
					stack_operator.push(x)

	for x in range(stack_operator.len):
		stack_hasil.push(stack_operator.pop())

	print("\n\t\t-- HASIL KONVERSI KE POSTFIX --\n")
	stack_hasil.printR()

	ulangi = input("Gunakan ulang program? [y / n] : ")