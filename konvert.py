from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.geometry('500x200')
root.title('Angka Terbilang')

def konversi(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = " "
    if x <= 0:
        hasil += "Bilangan Haruslah Positif\ndan Bilangan Asli"
    elif x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += konversi(x-10) + " belas\n"
    elif x < 100:
        hasil += konversi(int(x/10)) + " puluh\n" + konversi(x%10)
    elif x < 200 :
        hasil += "seratus " + konversi(x-100)
    elif x < 1000 :
        hasil += konversi(int(x/100)) + " ratus\n" + konversi(x%100)
    elif x < 2000 :
        hasil += "seribu " + konversi(x-1000)
    elif x < 1000000 :
        hasil += konversi(int(x/1000)) + " ribu\n" + konversi(x%1000)
    elif x < 1000000000 :
        hasil += konversi(int(x/1000000)) + " juta\n" + konversi(x%1000000)
    elif x >= 1000000000 :
        hasil += konversi(int(x/1000000000)) + " milyar\n" + konversi(x%1000000000)
    return hasil

def konversia():
    a = kolom.get()
    b = int(a)
    c = konversi(b)

    label.insert(END, c)

kolom = Entry(root, width=70)
kolom.grid(row=0, column=0, padx=3)

tombol = Button(root, text='Konversi', bg='black', fg='green', command=konversia)
tombol.grid(row=0, column=1, sticky=W)

label= Text(root, width=50, height=10)
label.grid(row=1, columnspan=2, pady=3)

root.mainloop()