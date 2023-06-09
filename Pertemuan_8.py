# print('Hello World')
# nama = "hajar nimpuno adi"
# print(nama)     # Menampilakan variable nama apa adanya
# print(nama.upper()) # Menampilkan variable nama dengan huruf BESAR
# print(nama.capitalize())
# print(nama.title())
# print(nama.split(" "))

# print ('1')
# print(1)
# print(1.5)

# #Tambah
# print (10 + 5)
#  #Kurang
# print (10 - 5)
# # Perkalian
# print( 10*5)
# #Pembagian
# print (10 / 5)
# #Sisa Bagi
# print(10 % 3)

# sapa = "Hajar"
# print(sapa)
# print(sapa)
# print(sapa)
# print(sapa)
# print(sapa)
# print(sapa)

# nama_depan = "Hajar"
# nama_tengah = "Nimpuno"
# nama_belakang = "Adi"

# sapa = "Halooo  " + nama_depan + " "+ nama_tengah + " "+ nama_belakang
# print (sapa)

# gabungan = f"Halooo {nama_depan} {nama_tengah} {nama_belakang}"
# print(gabungan)


# # Belajar menggunakan input data
# print("Silakan masukkan nama anda : ")
# nama = input()
# print (f"Hello {nama}, Selamat belajar")

# print("Angka pertama : ")
# x = int(input())
# print ("Angka kedua")
# y = int(input())
# hasil = x + y
# print(f"{x} + {y} = {hasil}")

# Operator perbandingan

# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan

# print (1 > 4)
# print (1 < 3)
# print ('hajar' == 'Hajar')

# # Statement IF

# # if kondisi:
#     # melakukan apa?
#     # dan seterusnya.

# orang = 1000
# drakula = 100

# if orang < drakula:
#     print("Semua orang akan mati")

# if orang > drakula:
#     print("drakula akan musnah")

# # Statement IF-ELSE
# logika = False
# # if logika == True:
# #     print("Selamat, anda memenangkan hadiah")
# # if logika == False:
# #     print("Mohon maaf, anda kalah")


# if logika == True:
#     print("Selamat, anda menang")
# else:
#     print("Mohon maaf, anda kalah")

# Statment ELIF
# menu_pilihan = input("Silakan pilih menu [1-3] : ")

# if menu_pilihan == "1":
#     print ('Anda memilih menu 1')

# if menu_pilihan == "2":
#     print ('Anda memilih menu 2')

# if menu_pilihan == "3":
#     print ('Anda memilih menu 3')

# else:
#     print('Menu tidak tersedia')

# menu_pilihan = input("Silakan pilih menu [1-3] : ")
# if menu_pilihan == "1":
#     print ('Anda memilih menu 1')
# elif menu_pilihan == "2":
#     print ('Anda memilih menu 2')
# elif menu_pilihan == "3":
#     print ('Anda memilih menu 3')
# else:
#     print('Menu tidak tersedia')

# #  L I S T
# nama = ['andi', 'budi', 'cinta']
# print(nama)
# nama.append('dondi')
# print(nama)
# nama.append('evando') # Menambahkan data di list
# print(nama)
# nama.remove('evando') #Menghapus data dari list
# print(nama)
# print (len(nama)) # Mengetahui jumlah yang terdapat dalam list.

# print(nama[:2])

# nama = ['andi', 'budi', 'cinta', 'dondi', 'evando']

# # # Cara mengakses semua nama :
# # print(nama[0])
# # print(nama[1])
# # print(nama[2])
# # print(nama[3])
# # print(nama[4])

# for x in nama:
#     print(f'{x}')


# Belajar RANGE
# angka = [1,2,3,4,5,6,7,8,9,10]
# angka = range(1,11)
# for no in angka:
#     print(no)

# for no in range(1, 11):
#     print(no)

# # While - Loop
# while kondisi:
#     isi dari while

# data = ""
# while data !="x":
#     print("perulangan")
#     data = input('data : ')

# # # CONTINUE
# for i in range(1, 100):
#     if i % 2 == 0:
#         continue
#     print(i)

# BREAK
# for i in range(1, 100):
#     if i % 50 == 0:
#         break
#     print(i)

# TUPLE
# customer = ('Anto', 'Budi', 'Cindi', 'Dondi')
# print(customer[2])
# print(customer[1])
# print(customer[3])

# SET

# List => [ ]
# Tuple => ( )
# Set   => {  } - Tidak menerima duplikasi
# Tidak bisa akses data menggunakan index
# Tidak menggunakan append tapi => ADD
# Tidak bisa mengubah data.
# Menambah data atau menghapus data.

# nama = {"Anto", "Budi", "Cintia", "Budi"}
# print(nama)
# nama.add("Hajar")
# nama.remove("Anto")
# print(nama)

# for data in nama:
#     print(data)

# METHOD
# nama=[]
# nama.append("Hajar")
# for data in nama:
#     print(data)

# nama.append("Nimpuno")
# for data in nama:
#     print(data)

# nama.append("Adi")
# for data in nama:
#     print(data)


# nama = []

# def print_nama():
#     for data in nama:
#         print(data)

# nama.append("Hajar")
# print_nama()

# nama.append("Nimpuno")
# print_nama()

# nama.append("Adi")
# print_nama()


# METHOD Paremeter
# def sapa(nama_depan, nama_belakang):
#     print(f'Hello {nama_depan} {nama_belakang}')

# sapa("Hajar", "Nimpuno")
# sapa("Aditya", "Pawaid")


# Default Argument Value
# def sapa(nama_depan="Mas / Mbak", nama_belakang=""):
#     print(f'Hello {nama_depan} - {nama_belakang}')

# sapa(nama_belakang="Sahara")
# sapa("sahara","eka")

# def jumlah(satu, dua, tiga=0, empat=0):
#     total = satu + dua + tiga + empat
#     print(f'Total {[satu, dua, tiga, empat]} = {total}')

# jumlah (10, 10)

# # Argument LIST ####
# def jumlah(*list_angka):
#     total = 0
#     for angka in list_angka:
#         total = total + angka
#     return (list_angka, total)
#     print (f'Total {list_angka} = {total}')

# list_angka, total = jumlah (10, 10, 10 ,10, 10 ,10)

# print(total)
# print(f'Total {list_angka} = {total}')


# ### DICTIONARY => DICT
# mahasiswa = {"Nama":"Hajar", "Usia": 30, "Alamat" : "Bantul"}

# nama = mahasiswa["Nama"]
# usia = mahasiswa["Usia"]
# alamat = mahasiswa["Alamat"]

# for key in mahasiswa:
#     value = mahasiswa[key]
#     print(f'{key}:{value}')


# Module dan Function.
# import function
# from function import sapa
from function import sapa as say

menyapa = say('Hajar')
print(menyapa)
