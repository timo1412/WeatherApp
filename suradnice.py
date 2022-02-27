from tkinter import *
from tkinter import messagebox
from data import Data

class Suradnice():
    def __init__(self):
        self.gps = []
        self.weatherParams = {}

    def savingGPS(self):
        self.lonEntrTxt = self.longtitude.get()
        self.latEntrTxt = self.latitude.get()
        if self.lonEntrTxt == "" or self.latEntrTxt == "":
            print("Nenechávaj prazdne miesta")
        else:
            with open("GPS.txt", mode="w") as dataFile:
                dataFile.write(f"{self.lonEntrTxt} {self.latEntrTxt}")
                # vyska.delete(0,END)
                # sirka.delete(0,END)

    def nacitajSuradnice(self):
        # ošetrit viacrozmerny string
        with open("GPS.txt") as file:
            datatxt = file.read()
        self.gps = datatxt.split()

    def getSuradnice(self):
        return self.gps

    def kontrolaSuradnic(self):
        try:
            if (int(self.latitude.get()) < 180 and int(self.latitude.get()) > -180):
                if (int(self.longtitude.get()) < 90 and int(self.longtitude.get()) > -90):
                    self.savingGPS()
                    print("sprven suradnice ")
                    self.oknoSuradnic.destroy()
                    return True

                else:
                    messagebox.showerror(title="ERROR", message="Nespravne zadaná šírka")
                    return NONE
            else:

                messagebox.showerror(title="ERROR", message="Nespravne zadaná výška ")
                return NONE
        except ValueError:
            messagebox.showerror(title="", message="Nenechávaj prazdne miesta")
            return NONE



    def oknoSuradnic(self):

        self.nacitajSuradnice()

        self.oknoSuradnic = Tk()
        self.oknoSuradnic.title("Miesto predpovede")
        self.oknoSuradnic.config(pady=20, padx=20)

        self.vyskaLabael = Label(text="Zadaj Zemepisnú širku oblasti (lat) 48:")
        self.vyskaLabael.grid(row=1, column=1)

        self.sirkaLabel = Label(text="Zadaj Zemepisnú dĺžku oblasti (lon) 18:")
        self.sirkaLabel.grid(row=2, column=1)

        self.longtitude = Entry(width=50)
        self.longtitude.insert(END, f"{self.gps[0]}")
        self.longtitude.grid(row=1, column=2)
        self.longtitude.focus()

        self.latitude = Entry(width=50)
        self.latitude.insert(END, f"{self.gps[1]}")
        self.latitude.grid(row=2, column=2)
        self.latitude.focus()

        self.hladajButton = Button(text="Hladaj", highlightthickness=0, command=self.kontrolaSuradnic)
        self.hladajButton.grid(row=3, column=1)

        self.oknoSuradnic.mainloop()

