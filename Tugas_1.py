nama_pendek_anda = "imanudin"

while True:
    masukan_nama = input("Masukkan nama anda : ")
    if masukan_nama.lower() == nama_pendek_anda.lower():
        break
    else:
        print("silahkan coba lagi")

print()

angka_user = int(input("Masukkan angka: "))

for i in range(1, 11):
    print(f"{angka_user} x {i} = {angka_user * i}")