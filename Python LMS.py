import datetime   
import os
os.getcwd()
 
class LMS:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n",""),"lender_name": "","Issue_date":"","Status":"Ada"}})
            id = id + 1

    def display_books(self):
        print("--------------------Daftar Buku--------------------")
        print("ID Buku", "\t","Judul")
        print("---------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"), "- [",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Masukkan ID buku: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Ada":
                print(f"Buku ini telah dipinjam oleh {self.books_dict[books_id]['lender_name']} \ di tanggal {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Ada":
                your_name = input("Masukkan nama anda: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Sudah Dipinjamkan"
                print("Buku berhasil dipinjamkan!!! \n")
        else:
            print("ID buku tidak ditemukan")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Masukkan judul buku: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Judul buku terlalu panjang! batas jumlah huruf untuk judul adalah 25")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as b:
                b.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Ada'}})
                print(f"Buku '{new_books}' telah berhasil ditambahkan!")

    def return_books(self):
        books_id = input("Masukkan ID buku: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Ada":
                print("Buku ini belum dipinjamkan dan masih di perpustakaan ZETA. Mohon periksa ulang ID buku")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Ada":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Ada"
                print("Buku berhasil dikembalikan!")
        else:
            print("ID buku tidak ditemukan, mohon periksa kembali")

if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.txt", "ZETA")
        press_key_list = {"D": "Daftar Buku", "M": "Minjam Buku", "N": "Nambah Buku", "O": "Mengembalikan Buku", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Selamat datang ke Sistem Manajemen Perpustakaan {mylms.library_name}---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "m":
                print("\nMenu Pilihan : Minjam Buku\n")
                mylms.Issue_books()
                
            elif key_press == "n":
                print("\nMenu Pilihan : Nambah Buku\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nMenu Pilihan : Daftar Buku\n")
                mylms.display_books()
            
            elif key_press == "o":
                print("\nMenu Pilihan : Mengembalikan Buku\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Sistem Error, Mohon Periksa Ulang!!!!")
