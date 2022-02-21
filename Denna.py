from tkinter import *
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Denna(Toplevel):
    def __init__(self , paData):
        self.data = paData


    def zobraz_okno(self):
        self.window = Toplevel()
        self.window.config(pady=50 , padx=50)
        self.window.title("Okno denne")
        self.window.minsize(width=1600,height=900)


    def dniTyzdna(self, index):

        for index in range(0,6):

            canvasDatumDna = Canvas(self.window, width=300, height=60)
            ts1 = int(f"{self.data[index]['dt']}")
            datum = datetime.utcfromtimestamp(ts1).strftime('%d.%m')
            canvasDatumDna.create_text(100, 50, text=f"{datum} ", width=200,font=("Arial", 15, "bold"))
            canvasDatumDna.grid(row=1, column=index)

            ts1 = int(f"{self.data[index]['sunrise']}")
            datum1 = datetime.utcfromtimestamp(ts1).strftime( '%H:%M ')
            self.vychod = Label(self.window, text=f" Východ slnka {datum1} ")
            self.vychod.grid(row=2, column=index)

            ts2 = int(f"{self.data[index]['sunset']}")
            datum2 = datetime.utcfromtimestamp(ts2).strftime(' %H:%M ')
            self.zapad = Label(self.window, text=f" Západ slnka {datum2} ")
            self.zapad.grid(row=3, column=index)

            self.maxtemp = Label(self.window,
                                 text=f" Maximálna teplota {round(self.data[index]['temp']['max'] - 273.1500, 1)} ")
            self.maxtemp.grid(row=4, column=index)

            self.mintemp = Label(self.window,
                                 text=f" Minimálna teplota {round(self.data[index]['temp']['min'] - 273.1500, 1)} ")
            self.mintemp.grid(row=5, column=index)

            self.nightTemp = Label(self.window,
                                   text=f" Nočná teplota {round(self.data[index]['temp']['night'] - 273.1500, 1)} ")
            self.nightTemp.grid(row=6, column=index)

            self.dayTemp = Label(self.window,
                                 text=f" Denná teplota {round(self.data[index]['temp']['day'] - 273.1500, 1)} ")
            self.dayTemp.grid(row=7, column=index)

            self.mornTemp = Label(self.window,
                                  text=f" Ranná teplota {round(self.data[index]['temp']['morn'] - 273.1500, 1)} ")
            self.mornTemp.grid(row=8, column=index)

            self.pocitovaDenna = Label(self.window,
                                       text=f" Pocitova denná {round(self.data[index]['feels_like']['day'] - 273.1500, 1)} ")
            self.pocitovaDenna.grid(row=9, column=index)

            self.pocitovaNocna = Label(self.window,
                                       text=f" Pocitová nočná {round(self.data[index]['feels_like']['night'] - 273.1500, 1)} ")
            self.pocitovaNocna.grid(row=10, column=index)

            self.tlak = Label(self.window, text=f" Tlak {self.data[index]['pressure']} ")
            self.tlak.grid(row=11, column=index)

            self.vlhkost = Label(self.window, text=f" Vlhkost {self.data[index]['humidity']} ")
            self.vlhkost.grid(row=12, column=index)

            self.rychlostVetra = Label(self.window, text=f" Rýchlosť vetra {self.data[index]['wind_speed']} ")
            self.rychlostVetra.grid(row=13, column=index)

            self.oblacnost = Label(self.window, text=f" Oblačnosť {self.data[index]['clouds']} ")
            self.oblacnost.grid(row=14, column=index)

            try:
                self.snezenie = Label(self.window, text=f" Sneženie v % {self.data[index]['snow']} ")
                self.snezenie.grid(row=15, column=index)
            except KeyError:
                self.snezenie = Label(self.window, text=" Sneženie v % 0 ")
                self.snezenie.grid(row=15, column=index)

            try:
                self.dazd = Label(self.window, text=f" Dážd´ v % {self.data[index]['rain']} ")
                self.dazd.grid(row=16, column=index)
            except KeyError:
                self.dazd = Label(self.window, text=" Dážd´ v % 0 ")
                self.dazd.grid(row=16, column=index)

    def vypisData(self):
        print(self.data)

    def zavrietOkno(self):
        #self.window.mainloop()
        self.window.destroy()

    def tlacitkoBack(self):
        buttSpat = Button( self.window , text="BACK" , highlightthickness=0 , command=self.zavrietOkno)
        buttSpat.grid(row=0,column=0)

    def grafDazda(self):
        cas = []
        oblacnost = []
        for i in range(0, 7):
            cas.append(datetime.utcfromtimestamp(int(f"{self.data[i]['dt']}")).strftime('%m/%d'))
            try:
                oblacnost.append(self.data[i]['rain'])
            except KeyError:
                oblacnost.append(0)
        print(cas)
        data2 = {'Čas': cas,
                 'Dazd': oblacnost
                 }
        matplotlib.use("TkAgg")

        figure = Figure(figsize=(8, 4), dpi=100)
        figure.suptitle(
            "Pravdepodobnosť dažda")

        plot = figure.add_subplot(1, 1, 1)
        plot.plot(color="red", marker="o")

        plot.plot(data2['Čas'],
                  data2['Dazd'],
                  color="blue", marker="o")
        figure.autofmt_xdate()  # automatické naklonenie dátumov
        plot.grid()  # zobrazenie mriežky

        canvas = FigureCanvasTkAgg(figure, self.window)
        canvas.get_tk_widget().grid(row=25, column=3, columnspan=3)

    def grafTeplot(self):
        cas = []
        teploty = []
        for i in range(0, 7):
            cas.append(datetime.utcfromtimestamp(int(f"{self.data[i]['dt']}")).strftime('%m/%d'))
            teploty.append(round(self.data[i]['temp']['day'] - 273.1500, 1))
        print(cas)
        data2 = {'Čas': cas,
                 'Teplota_dni': teploty
                 }
        matplotlib.use("TkAgg")

        figure = Figure(figsize=(8, 4), dpi=100)
        figure.suptitle(
            "Teploty dňa")

        plot = figure.add_subplot(1, 1, 1)
        plot.plot(color="red", marker="o")

        plot.plot(data2['Čas'],
                  data2['Teplota_dni'],
                  color="red", marker="o")
        figure.autofmt_xdate()  # automatické naklonenie dátumov
        plot.grid()  # zobrazenie mriežky

        canvas = FigureCanvasTkAgg(figure, self.window)
        canvas.get_tk_widget().grid(row=25, column=0, columnspan=3)