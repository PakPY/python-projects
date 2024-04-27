def tambah(x, y):
    z = x + y
    return z


def kurang(x, y):
    z = x - y
    return z


def kali(x, y):
    z = x * y
    return z


def bagi(x, y):
    z = x / y
    return z


print("APLIKASI KALKULATOR SEDERHANA\n")
angka1 = int(input("angka 1\t\t\t: "))
pilih = str(input("pilih operator \n(+, -, *, /)\t: "))
angka2 = int(input("angka 2\t\t\t: "))

if pilih == "+":
    jumlahin = tambah(angka1, angka2)
    print("\nHASIL\n%d + %d = %d" % (angka1, angka2, jumlahin))

elif pilih == "-":
    kurangin = kurang(angka1, angka2)
    print("\nHASIL\n%d - %d = %d" % (angka1, angka2, kurangin))

elif pilih == "*":
    kaliin = kali(angka1, angka2)
    print("\nHASIL\n%d * %d = %d" % (angka1, angka2, kaliin))

elif pilih == "/":
    bagiin = bagi(angka1, angka2)
    print("\nHASIL\n%d / %d = %0.2f" % (angka1, angka2, bagiin))

else:
    print("\nhmm... tulis operator yg tepat yaa... :)")
