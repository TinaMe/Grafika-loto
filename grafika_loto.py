import Tkinter as Tk
import tkMessageBox
import random

seznam_stevil = []

def klik_gumba():

    vpisane_stevilke = int(stevilo_cifer.get())
    for i in range(0, vpisane_stevilke):
        stevila = random.randint(1, 39)
        while stevila in seznam_stevil:
            stevila = random.randint(1, 39)

        seznam_stevil.append(stevila)

    seznam_stevil.sort()
    tkMessageBox.showinfo("Loto stevilke so:", seznam_stevil)

main_window = Tk.Tk()

greeting = Tk.Label(main_window, text="Pozdravljeni v programu Generator loto stevil!")
navodilo = Tk.Label(main_window, text="Prosimo vpisite, koliko nakljucnih loto stevil zelite:")
stevilo_cifer = Tk.Entry(main_window)

greeting.pack()
navodilo.pack()
stevilo_cifer.pack()

gumb = Tk.Button(main_window, text="Izpisi!", command=klik_gumba)
gumb.pack()





main_window.mainloop()