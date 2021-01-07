import tkinter


class Opdr1:
    def __init__(self):
        #Aanmaken main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("200x125")

        #2 frames verdelen
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        #Adres een text variabele maken, het adres ophalen als op button
        # word geklikt
        self.adres = tkinter.StringVar()
        self.adres_label = tkinter.Label(self.top_frame,
                                         textvariable=self.adres)
        self.adres_label.pack()

        #Button aanmaken dat gegevens weergeeft als je erop klikt
        self.show_button = tkinter.Button(self.bot_frame,
                                          text="Show Info",
                                          command=self.info)
        self.show_button.pack()

        #Button aanmaken dat programma sluit als erop wordt geklikt
        self.quit_button = tkinter.Button(self.bot_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)
        self.quit_button.pack()

        self.top_frame.pack()
        self.bot_frame.pack()

        self.main_window.mainloop()

    def info(self):
        #Alle gegevens wat moet worden weergegeven
        self.text = "Luc Hengeveld\nHalve Morgen 52\nWestervoort, 6931XN"
        self.adres.set(self.text)


info = Opdr1()
