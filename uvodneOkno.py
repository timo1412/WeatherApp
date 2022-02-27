from tkinter import *
from Hodinova import Hodinova
from Denna import Denna
from Aktualna import Aktualna


class UvodneOkno():
    def __init__(self , paData):
        self.data = paData
        print(self.data)

    def zobrazAktualna(self):
        # aktualna.oknoNaTeplotu()
        self.aktualna.zobraz_okno()
        self.aktualna.zobrazData()
        self.aktualna.tlacitkoBack()
        # aktualna.vypisData()
    def zobrazDenna(self):
        self.denna.zobraz_okno()
        self.denna.dniTyzdna(1)
        self.denna.tlacitkoBack()
        self.denna.grafTeplot()
        self.denna.grafDazda()
    def zobrazHod (self):
        self.hodinova.zobraz_okno()
        self.hodinova.hodinyDna()
        self.hodinova.tlacitkoBack()
        self.hodinova.grafTeplot()
        self.hodinova.grafOblacnosti()

    def rozdelData(self):
        # =============ROZDELENIE DAT==============
        self.hodinoveData = self.data["hourly"]
        self.denneData = self.data["daily"]
        self.aktualne = self.data["current"]

    def vytvorPredpovede(self):
        # =============VYTVORENIE OBJEKTOV JEDNOTLIVYCH PREDPOVEDI==============
        self.aktualna = Aktualna(self.aktualne)
        self.denna = Denna(self.denneData)
        # denna.zobraz_okno()
        self.hodinova = Hodinova(self.hodinoveData)
        # hodinova.zobraz_okno()

    def vytvorUvodneOkno(self):
        self.uvodne_oko = Tk()
        self.uvodne_oko.title("Uvodné okno")
        self.uvodne_oko.config(padx=20, pady=20)

        def oknoDestroy():
            self.uvodne_oko.destroy()

        self.buttonExit = Button(text="EXIT", highlightthickness=0, command=oknoDestroy, pady=10, padx=10)
        self.buttonExit.grid(row=0, column=3)

        self.imgAktu = PhotoImage(file="images.png")
        self.aktual_Button = Button(image=self.imgAktu, highlightthickness=0, command=self.zobrazAktualna)
        self.aktual_Button.grid(row=2, column=0)

        self.imgDenna = PhotoImage(file="images12.png")
        self.denna_Button = Button(image=self.imgDenna, highlightthickness=0, command=self.zobrazDenna)
        self.denna_Button.grid(row=2, column=1)

        self.imgHod = PhotoImage(file="images1234.png")
        self.hodin_Button = Button(image=self.imgHod, highlightthickness=0, command=self.zobrazHod)
        self.hodin_Button.grid(row=2, column=2)

        self.labelAktualna = Label(text="Aktuálna", font=("Arial", 20, "bold"))
        self.labelAktualna.grid(row=1, column=0)

        self.labelDenna = Label(text="Denná", font=("Arial", 20, "bold"))
        self.labelDenna.grid(row=1, column=1)

        self.labelHodinova = Label(text="Hodinová", font=("Arial", 20, "bold"))
        self.labelHodinova.grid(row=1, column=2)

        self.uvodne_oko.mainloop()
