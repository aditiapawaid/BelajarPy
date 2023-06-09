# # from tkinter import *
# # # main / root
# # # main_window = Tk()

# # from tkinter import *
# # main_window = Tk()
# # lebar=1000
# # tinggi=600
# # x=100
# # y=100
# # ## Cara disable maximize window
# # # main_window.resizable(0,0)
# # main_window.minsize(lebar,tinggi)

# # main_window.maxsize(lebar,tinggi)
# # # Mengganti Title dari Main Window
# # main_window.title("Belajar package TKINTER")
# # # Memposisikan Main Window tepat di tengah-tengah layar
# # screenwidht=main_window.winfo_screenwidth()
# # screenheight=main_window.winfo_screenheight()
# # new_x = int((screenwidht/2) - (lebar/2))
# # new_y = int((screenheight/2) - (tinggi/2))
# # main_window.geometry(f"{lebar}x{tinggi}+{new_x}+{new_y}")
# # main_window.mainloop()

# from tkinter import*
# # main / root
# main_window = Tk()
# main_window.geometry("500x500+600+400")
# # Mengganti Title dari Main Window
# main_window.title("Belajar package TKINTER")
# # Menambahkan event Button
# # def eventButton(event):
# #     print(event)
# #     print(f"Koordinat kursor ( {event.x} , {event.y} )")
# # main_window.bind("<Button>", eventButton)

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
from tkinter import*
# main / root
main_window = Tk()
main_window.geometry("500x500+200+200")
# Mengganti Title dari Main Window
main_window.title("Belajar package TKINTER")

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)

button1 = Button(text="Button_1")
button2 = Button(text="Button_2")
button3 = Button(text="Button_3")
button4 = Button(text="Button_4")

button1.grid(column=0, row=0, sticky="wens")
button2.grid(column=1, row=0, sticky="wens")
button3.grid(column=2, row=0, sticky="wens", columnspan=3)
button4.grid(column=0, row=1, sticky="wens", columnspan=5)
main_window.mainloop()