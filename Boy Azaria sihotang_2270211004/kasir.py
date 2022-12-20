menu = {
      "Burger Queen"  :13000,
    "Friench Fries" :20000,
    "Lemon Tea"     :10000,
    "Ice Cola Cola" :14000,
    "Jasmine Tea"   :13000,
}
print("==================Daftar Menu==================")
for i in menu :
    print("Daftar Menu : ", i,"\t Harga :",menu[i])
print("Pembrlian diatas Rp80.000,- mendapatkan diskon 15%")
print("===========SELAMAT DATANG DIKEDAI KOPI KALIMALANG=====================")
beli =input("Pilih Menu :")
jumlah = int(input("Jumlah Pesanan : "))
namapemesan = input("Nama Pemesan:")
notelp = input("No Telp:")
bayar = int(jumlah* menu[beli])

if  bayar > 80000 :
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

import time
tanggal = time.strftime("%d-%m-%y %H : %M : %S")
print(tanggal)
print(type(tanggal))

print("================== Detail Pembayaran======================")
print("Nama Pemesan              : ",namapemesan)
print("No Telp                   : ",notelp)
print("Menu yang dipesan         : ",beli)
print("Jumlah yang dipesan       : ",jumlah)
print("Total Biaya               : ",bayar)
print("Total yang harus dibayar  : ",total)
