from tkinter import *
from datetime import datetime , timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.figure import Figure





class Hodinova(Toplevel):
    def __init__(self , paData):
        self.data = paData


    def zobraz_okno(self):
        self.window = Tk()
        self.window.config(pady=50 , padx=50)
        self.window.title("Okno Hodiova")
        self.window.minsize(width=1600,height=900)



    def hodinyDna(self):

        riadok = 1
        stlpec = 1
        for index in range (0,26):
            if(index%9 == 0):
                riadok +=6
                stlpec = 1
            ts1 = int(f"{self.data[index]['dt']}")
            datum1 = datetime.utcfromtimestamp(ts1).strftime('%d.%m %H:%M ')
            self.datum = Label(self.window, text=f"{datum1}" , font=("Arial", 10,"bold"))
            self.datum.grid(row=riadok, column=stlpec)

            self.teplota = Label(self.window, text=f"Teplota je : { round(self.data[index]['temp'] - 273.1500 , 1) }" , font=("Arial", 10,"bold"))
            self.teplota.grid(row=riadok+1, column=stlpec)

            self.pocitovaTeplota = Label(self.window, text=f"Pocitová teplota je : { round(self.data[index]['feels_like'] - 273.1500 , 1) }" , font=("Arial", 10,"bold"))
            self.pocitovaTeplota.grid(row=riadok+2, column=stlpec)

            self.oblacnost = Label(self.window, text=f"Oblačnosť v % {self.data[index]['clouds']}" , font=("Arial", 10,"bold"))
            self.oblacnost.grid(row=riadok+3, column=stlpec)

            self.novyRiadok = Label(self.window, text=f"                                          ")
            self.novyRiadok.grid(row=riadok+4 , column=stlpec)
            stlpec +=1

    def grafTeplot(self):
        cas = []
        teploty = []
        for i in range(0, 24):
            cas.append(datetime.utcfromtimestamp(int(f"{self.data[i]['dt']}")).strftime('%H:%M '))
            teploty.append(round(self.data[i]['temp'] - 273.1500 , 1))
        print(cas)
        data2 = {'Čas': cas ,
                 'Teplota_dni':teploty
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
        canvas.get_tk_widget().grid(row=25, column=0, columnspan=5)


    def grafOblacnosti(self):
        cas = []
        oblacnost = []
        for i in range(0, 24):
            cas.append(datetime.utcfromtimestamp(int(f"{self.data[i]['dt']}")).strftime('%H:%M '))
            oblacnost.append(self.data[i]['clouds'])
        print(cas)
        print("OBLACNOST OBLACNOST")
        print(oblacnost)
        data2 = {'Čas': cas,
                 'Oblačnost': oblacnost
                 }
        matplotlib.use("TkAgg")

        figure = Figure(figsize=(8, 4), dpi=100)
        figure.suptitle(
            "Oblačnosť")

        plot = figure.add_subplot(1, 1, 1)
        plot.plot(color="red", marker="o")

        plot.plot(data2['Čas'],
                  data2['Oblačnost'],
                  color="Blue", marker="o")
        figure.autofmt_xdate()  # automatické naklonenie dátumov
        plot.grid()  # zobrazenie mriežky

        canvas = FigureCanvasTkAgg(figure, self.window)
        canvas.get_tk_widget().grid(row=25, column=5, columnspan=5)

    def zavrietOkno(self):
        #self.window.mainloop()
        self.window.destroy()

    def tlacitkoBack(self):
        buttSpat = Button( self.window , text="BACK" , highlightthickness=0 , command=self.zavrietOkno)
        buttSpat.grid(row=0,column=0)

    def vypisData(self):
        print(self.data)