pilih = input("Pilih Operasi ? (1 = Penjumlahan | 2 = Pengurangan) ")

try:
    val = int(pilih)
    print("yang di input adalah angka")
    print("nilai yang di input adalah ", val)
except ValueError:
    print("yang di input bukan angka")
    print("tidak ada nilai")

