"""Importeerd alles van tkinter"""
from tkinter import *

"""Maakt een GUI aan met de titel Rekenmachine"""
root = Tk()
root.title("Rekenmachine")

""" Maakt een tekstvak aan en een grid waar je buttons in kan gaan zetten
"""
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_klik(nummer):
    """ Als je op een knop drukt word de bijbehorende nummer doorgegeven en de waarde in het tekstvak opgeslagen.
    """
    waarde = e.get()
    e.delete(0, END)
    e.insert(0, str(waarde) + str(nummer))

def button_clear():
    """ Maakt het tekstvak leeg
    """
    e.delete(0, END)

def button_plus():
    """ Trekt 2 waarden op. Maakt van het eerst ingevoerde getal een global variabele zodat je gelijk hiermee
    kan verder rekenen. Slaat de variabele som op om de uiteindelijke berekening te doen bij def button_ant
    """
    getal1 = e.get()
    global eerstegetal
    global som
    som = "plus"
    eerstegetal = float(getal1)
    e.delete(0, END)

def button_min():
    """ Trekt 2 waarden van elkaar af. Maakt van het eerst ingevoerde getal een global variabele zodat je gelijk hiermee
    kan verder rekenen. Slaat de variabele som op om de uiteindelijke berekening te doen bij def button_ant
    """
    getal1 = e.get()
    global eerstegetal
    global som
    som = "min"
    eerstegetal = float(getal1)
    e.delete(0, END)

def button_keer():
    """ Vermenigvuldigd 2 waarden. Maakt van het eerst ingevoerde getal een global variabele zodat je gelijk hiermee
    kan verder rekenen. Slaat de variabele som op om de uiteindelijke berekening te doen bij def button_ant
    """
    getal1 = e.get()
    global eerstegetal
    global som
    som = "keer"
    eerstegetal = float(getal1)
    e.delete(0, END)

def button_delen():
    """ Deelt 2 waarden. Maakt van het eerst ingevoerde getal een global variabele zodat je gelijk hiermee
    kan verder rekenen. Slaat de variabele som op om de uiteindelijke berekening te doen bij def button_ant
    """
    getal1 = e.get()
    global eerstegetal
    global som
    som = "delen"
    eerstegetal = float(getal1)
    e.delete(0, END)

def button_ant():
    """ Kijkt wat je wilde doen (optellen/aftrekken/vermenigvuldigen/delen) en berekent dit door het eerste getal
    +-*/ het tweede getal te doen
    """
    getal2 = e.get()
    e.delete(0, END)

    if som == "plus":
        e.insert(0, eerstegetal + float(getal2))
    if som == "min":
        e.insert(0, eerstegetal - float(getal2))
    if som == "keer":
        e.insert(0, eerstegetal * float(getal2))
    if som == "delen":
        e.insert(0, eerstegetal / float(getal2))

""" Maakt alle verschillende buttons aan met textm bepaalde breedte en een bepaalde hoogte.
Lambda returned een waarde genaamd nummer, wat word gebruikt bij de functie button_klik om te kijken op welk cijfer
is geklikt. Elke knop roept een functie aan
"""
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_klik(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_klik(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_klik(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_klik(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_klik(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_klik(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_klik(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_klik(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_klik(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_klik(0))

button_plus = Button(root, text="+", padx=39, pady=20, command=button_plus)
button_min = Button(root, text="-", padx=41, pady=20, command=button_min)
button_keer = Button(root, text="X", padx=40, pady=20, command=button_keer)
button_delen = Button(root, text="/", padx=41, pady=20, command=button_delen)

button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_ant = Button(root, text="=", padx=91, pady=20, command=button_ant)

"""Zet de verschillende buttons in een grid. Row staat voor de y waarden en column voor de x waarden waar
de button komt te staan
"""
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_min.grid(row=6, column=0)
button_keer.grid(row=4, column=1)
button_delen.grid(row=4, column=2)

button_clear.grid(row=5, column=1, columnspan=2)
button_ant.grid(row=6, column=1, columnspan=2)

"""Zorgt ervoor dat de GUI open blijft en niet meteen sluit
"""
root.mainloop()