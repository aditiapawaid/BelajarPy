def menu():
    print ("Pilih Menu")
    print ("1. Daftar Buku")
    print ("2. Tambah Buku")
    print ("3. Hapus Buku")
    print ("4. Cari Buku")
    print ("5. Exit")

buku = open("namaa.txt","r+")

def daftarbuku():
    for x in buku:
        print (x)

def nambah():
    teks = buku.read()
    print(teks)
    a = input ("-nama buku :")
    teks = "{}\n".format (a)
    buku.write(teks)
    buku.close()
    print ("Terima kasih sudah menambahkan list buku :)")

def kurang():
    teks = buku.read()
    print(teks)
    b = input ("")
    del(b)
    print("Buku berhasil dihapus")


def nyari(g):
    filter_object = filter(lambda z: g in z, buku)
    p = list(filter_object)
    if(not p):
        print("Buku tidak ditemukan" )
    else:
        print("Buku '"+",".join (p)+ "' ditemukan.")

#main
menu()
j = input ("pilih layanan :")
if j == ("1"):
    daftarbuku()
elif j == ("2"):
    nambah()
elif j == ('3'):
    kurang() 
elif j == ('4'):
    g = input("-nama buku :")
    nyari(g)
elif j == ('5'):
    print ("terimakasi")
else :
    print ("input anda salah")