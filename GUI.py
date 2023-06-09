# from tkinter import *
# # main / root
# main_window = Tk()
# main_window.mainloop()

# from tkinter import *
# main_window = Tk()
# lebar=1000
# tinggi=600
# x=100
# y=100
# ## Cara disable maximize window
# # main_window.resizable(0,0)
# main_window.minsize(lebar,tinggi)

# main_window.maxsize(lebar,tinggi)
# # Mengganti Title dari Main Window
# main_window.title("Belajar package TKINTER")
# # Memposisikan Main Window tepat di tengah-tengah layar
# screenwidht=main_window.winfo_screenwidth()
# screenheight=main_window.winfo_screenheight()
# new_x = int((screenwidht/2) - (lebar/2))
# new_y = int((screenheight/2) - (tinggi/2))
# main_window.geometry(f"{lebar}x{tinggi}+{new_x}+{new_y}")
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# main_window.geometry("500x500+600+400")
# # Mengganti Title dari Main Window
# main_window.title("Belajar package TKINTER")
# # Menambahkan event Button
# def eventButton(event):
#     print(event)
#     print(f"Koordinat kursor ( {event.x} , {event.y} )")
# main_window.bind("<Button>", eventButton)

# # Menambahkan event KEY pada Main Window :
# def eventKey(event):
#     print(event)
#     print(f"Tombol yang ditekan adalah '{event.keysym}'")
# main_window.bind("<Key>", eventKey)
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# main_window.geometry("500x500+200+200")

# # Mengganti Title dari Main Window
# main_window.title("Belajar package TKINTER")
# # Menggunakan widget button dengan layout pack()
# button1 = Button(text="Button_1")
# button1.pack(side=TOP,fill=BOTH, padx=50, pady=100)
# main_window.mainloop()

'''
grid
'''
# from tkinter import*
# # main / root
# main_window = Tk()
# main_window.geometry("500x500+200+200")
# # Mengganti Title dari Main Window
# main_window.title("Belajar package TKINTER")

# main_window.columnconfigure(0, weight=1)
# main_window.columnconfigure(1, weight=1)
# main_window.columnconfigure(2, weight=1)
# main_window.columnconfigure(3, weight=1)
# main_window.columnconfigure(4, weight=1)

# main_window.rowconfigure(0, weight=1)
# main_window.rowconfigure(1, weight=1)

# button1 = Button(text="Button_1")
# button2 = Button(text="Button_2")
# button3 = Button(text="Button_3")
# button4 = Button(text="Button_4")

# button1.grid(column=0, row=0, sticky="wens")
# button2.grid(column=1, row=0, sticky="wens")
# button3.grid(column=2, row=0, sticky="wens", columnspan=3)
# button4.grid(column=0, row=1, sticky="wens", columnspan=5)
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# # Mengganti Title dari Main Window
# main_window.title("TKINTER")
# main_window.geometry("500x500+200+200")
# button = Button(text="My Button")
# # button.place(x=100, y=0, width=100, height=100,)
# button.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1 )

# main_window.mainloop()

'''
widget button
'''

# from tkinter import *
# # main / root
# main_window = Tk()
# def event_tekan():
#     label2 = Label(main_window, text="Tombol sudah ditekan ^-^")
#     label2.pack()

# tombol = Button(main_window,text='Tekan aku',command=event_tekan)

# tombol.pack()
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# # Deklarasi method
# def buttonclick():
#     print("My Button di klik")
# def klik_button2(x):
#     print(x)
# # Mengganti Title dari Main Window
# main_window.title("PRAKTIKUM GUI TKINTER")
# main_window.geometry("500x500+200+200")
# # Menambahkan widget BUTTON pada main window
# button = Button(main_window, text="My Button", activebackground="#ff0000", command=buttonclick)
# # button.place(x=100, y=0, width=100, height=100,)
# button.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1 )
# button2 = Button(main_window, text="Button_2", command=lambda: klik_button2("Button_2"))
# button2.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# # Mengganti Title dari Main Window
# main_window.title("PRAKTIKUM GUI TKINTER")
# main_window.geometry("500x400+200+200")
# # Menambahkan widget label pada main window
# label_1 = Label(text="Label 1", bg="#ff1710", height=20, width=40, anchor="sw")
# label_1.pack()
# main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# # Mengganti Title dari Main Window
# main_window.title("PRAKTIKUM GUI TKINTER")
# main_window.geometry("500x500+200+200")
# # Menambahkan widget entry
# entry1 = Entry(main_window, bd=10, font=("Verdana 15 underline"))
# entry1.pack()

# main_window.mainloop()

# from tkinter import*
# def buttonclicked():
#     # print ("Button di klik")
#     # myentry.delete(0,END)
#     print(myentry.get())
#     myentry.icursor(3)
#     print(myentry.index(INSERT))
#     myentry.insert(0, "+62")
#     myentry.select_adjust(4)
#     # myentry.delete(0,1)
#     # myentry.insert(0, "+62")

# # main / root
# main_window = Tk()
# # Mengganti Title dari Main Window
# main_window.title("PRAKTIKUM GUI TKINTER")
# main_window.geometry("500x500+200+200")
# # Menambahkan widget entry dan button
# myentry = Entry(main_window)
# myentry.pack()
# mybutton = Button(text="MyButton", command=buttonclicked)
# mybutton.pack()
# main_window.mainloop()

'''
widget text
'''

# from tkinter import*
# def klikbutton():
# # print("Klik Tombol")
# # mytext.insert("5.0", "Teks pada baris ke-5")
#  print(mytext.search("baris", "1.0", END))
# # main / root
# main_window = Tk()
# # Mengganti Title dari Main Window
# main_window.title("PRAKTIKUM GUI TKINTER")
# main_window.geometry("750x500+200+200")

# # Menambahkan widget TEXT
# mybutton = Button(text="MyButton", command=klikbutton)
# mybutton.pack(side=LEFT)
# myscrollbar = Scrollbar()
# mytext = Text(main_window, yscrollcommand=myscrollbar.set)
# mytext.pack(side=LEFT)
# mytext.insert("1.0", "Teks pada baris pertama \n")
# mytext.insert("2.0", "Teks pada baris kedua \n")
# mytext.insert("3.0", "Teks pada baris ketiga \n")
# mytext.insert("4.0", "Teks pada baris keempat \n")
# myscrollbar.pack(side=RIGHT, fill=Y)

# main_window.mainloop()

'''
widget menu
'''

# from tkinter import *
# # main / root
# main_window = Tk()
# menuBar = Menu()
# menuFile = Menu(menuBar)
# menuFile.add_command(label="New")
# menuFile.add_command(label="Open")
# menuFile.add_separator()
# menuFile.add_command(label="Exit")
# menuBar.add_cascade(label="File", menu=menuFile)
# menuEdit = Menu(menuBar)
# menuEdit.add_command(label="Undo")
# menuEdit.add_command(label="Cut")
# menuEdit.add_separator()
# menuEdit.add_command(label="Edit")
# menuBar.add_cascade(label="Edit", menu=menuEdit)
# main_window.config(menu=menuBar)

# main_window.mainloop()

'''
widget tabs 
'''

# from tkinter import *
# from tkinter import ttk
# main_window = Tk()
# main_window.geometry("750x250")

# my_notebook= ttk.Notebook(main_window)
# my_notebook.pack(expand=1,fill=BOTH)
# # Membuat Tab baru
# tab1= ttk.Frame(my_notebook)
# my_notebook.add(tab1, text= "Tab 1")
# tab2= ttk.Frame(my_notebook)
# my_notebook.add(tab2, text= "Tab2")
# # Membuat Label di dalam Tab

# Label(tab1, text= "TAB PERTAMA", font= ('Helvetica 20 bold')).pack()
# Label(tab2, text= "TAB KEDUA", font=('Helvetica 20 bold')).pack()
# main_window.mainloop()

'''
widget frame
'''

# import tkinter as tk
# # main / root
# main_window = tk.Tk()
# frameAtas = tk.Frame()
# frameAtas.pack()
# frameTengah = tk.Frame()
# frameTengah.pack()
# frameBawah = tk.Frame()
# frameBawah.pack()
# lblNama = tk.Label(frameAtas, text="Nama :")
# lblNama.pack(side=tk.LEFT)
# enNama = tk.Entry(frameAtas)
# enNama.pack(side=tk.LEFT)
# lblAlamat = tk.Label(frameAtas, text="Alamat :")
# lblAlamat.pack(side=tk.LEFT)
# enAlamat = tk.Entry(frameAtas)
# enAlamat.pack(side=tk.LEFT)
# lblUmur = tk.Label(frameTengah, text="Umur :")
# lblUmur.pack(side=tk.LEFT)
# enUmur = tk.Entry(frameTengah)
# enUmur.pack(side=tk.LEFT)
# imgDiri = tk.Canvas(frameTengah, width=300, height=200)
# imgDiri.create_rectangle(0,0,300,200)
# imgDiri.pack(side=tk.LEFT)
# btnOK = tk.Button(frameBawah, text="OK")
# btnOK.pack(side=tk.LEFT)
# main_window.mainloop()

'''
widget lanjutan combobox
'''

from tkinter import *
from tkinter import ttk
# main / root
main_window = Tk()
lblCaption = Label(text="Pilih bulan : ")
lblCaption.pack()
cmbBulan = ttk.Combobox(values=["Januari","Februari","Maret","April"])
cmbBulan.current(2)
cmbBulan.pack()

main_window.mainloop()