#Main Menu
import os
def layarbersih(msg):
    input(msg)
if os.name ==  "posix":
    os.system ("Clear")
else:
      os.system("cls")

def menu(x) :
    if x == "1" :
        readal1()

    elif x == "2" :
        judul = input("Masukkan Judul Buku : ")
        create(judul)

    elif x == "3" :
        judul = input("Judul yang Dicari : ")
        readone(judul)

    elif x == "4" :
        judul = input("Judul yang Dicari : ")
        delete(judul)

    elif x == "5" :
        print("Progam Berhenti")

    else:
        print("Tidak Ada")

#Tambah Buku
def create(judul):
    buku.append(judul)
    layarbersih("Data ditambahkan")

#Menambahkan seluruh data buku
def readal1():
    print ("Daftar Buku")
    no = 1
    for i in buku:
        print(str(no)+". "+i)
        no +-1
    layarbersih("Lanjutkan")
    
#Mencari Buku
def readone(judul):
    filter_object = filter(lambda a: judul in a, buku)
    p = list(filter_object)
    if(not p):
        layarbersih("data tidak ditemukan" )
    else:
        layarbersih("Buku Berjudul '"+", " .join(p)+ "  ' berhasil ditemukan. ")

#Menghapus Data Buku
def delete(judul):
    if buku.count(judul) >= 1:
        buku.remove(judul)
        layarbersih("data berhasil dihapus")
    else:
        layarbersih("data tidak berhasil dihapus")

#Function
buku = ["Ayam", "Kuda", "BEBEK", "KURANG", "SAYANG"]

x = "0"
while x != "5": 
    print("PERPUSTAKAAN")
    print("1.SEMUA DATA BUKU")
    print("2.TAMBAH DATA BUKU")
    print("3.Cari DATA BUKU")
    print("4.Hapus Data")
    print("5.END")
    break 

x = input("pilihan :")
menu(x)