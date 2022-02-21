from tkinter import *
from datetime import datetime

import os

class Aktualna(Toplevel):
    def __init__(self , paData):
        self.data = paData

    def zobraz_okno(self):
        self.window = Toplevel()
        self.window.config(pady=50 , padx=50 , )
        self.window.title("Okno aktualna")
        self.window.minsize(width=1600,height=900)



    def vypisData(self):
        print(self.data)

    def zobrazData(self):
        # self.ImgBg = PhotoImage(file="index159.png")
        # canvas = Canvas(self.window, width=15000, height=8000)
        # canvas.create_image(1500,800,image=self.ImgBg)
        # canvas.grid(row=0,column=0,rowspan=10,columnspan=10)

        canvasRychlostVetra = Canvas(self.window, width=300, height=60)
        canvasRychlostVetra.create_text(100, 50, text=f"Rýchlosť vetra {self.data[ 'wind_speed' ]} ", width=200, font=("Arial", 15, "bold"))
        canvasRychlostVetra.grid(row=1, column=3)
        self.ImgWindSpeed = PhotoImage(file="index632159.png")
        tampBut = Button(self.window, image=self.ImgWindSpeed, highlightthickness=0)
        tampBut.grid(row=2, column=3)


        canvasOblacnost = Canvas(self.window, width=300, height=60)
        canvasOblacnost.create_text(80, 50, text=f"Oblačnosť : {self.data[ 'clouds' ]}", width=200, font=("Arial", 15, "bold"))
        canvasOblacnost.grid(row=1 , column=4 )
        self.ImgClouds = PhotoImage(file="images369.png")
        tampBut = Button(self.window, image=self.ImgClouds, highlightthickness=0)
        tampBut.grid(row=2, column=4)


        canvasVychod = Canvas(self.window, width=300, height=60)
        ts1 = int(f"{self.data['sunrise']}")
        casVychod = datetime.utcfromtimestamp(ts1).strftime('%H:%M ')
        canvasVychod.create_text(110, 50, text=f"Vychod slnka : {casVychod}", width=260,font=("Arial", 15, "bold"))
        canvasVychod.grid(row=1, column=1)

        self.ImgSunRise = PhotoImage(file="98712.png")
        tampBut = Button(self.window, image=self.ImgSunRise, highlightthickness=0)
        tampBut.grid(row=2, column=1)



        canvasZapad = Canvas(self.window, width=300, height=60)
        ts1 = int(f"{self.data['sunset']}")
        casZapad = datetime.utcfromtimestamp(ts1).strftime('%H:%M ')
        canvasZapad.create_text(110, 50, text=f"Zapad slnka : {casZapad}", width=260, font=("Arial", 15, "bold"))
        canvasZapad.grid(row=1, column=2)

        self.ImgSunSet = PhotoImage(file="index63514.png")
        tampBut = Button(self.window, image=self.ImgSunSet, highlightthickness=0)
        tampBut.grid(row=2, column=2)

        canvasTeplota = Canvas(self.window, width=300, height=60)
        canvasTeplota.create_text(80, 50, text=f"Teplota : { round(self.data['temp'] - 273.1500 ,1) } C°", width=200,font=("Arial", 15, "bold"))
        canvasTeplota.grid(row=3, column=2 )

        canvasPocitovaTeplota = Canvas(self.window, width=400, height=60)
        canvasPocitovaTeplota.create_text(180, 50, text=f"Pocitová teplota : {round(self.data['feels_like'] - 273.1500, 1)} C°", width=300,font=("Arial", 15, "bold"))
        canvasPocitovaTeplota.grid(row=4, column=2)

        self.ImgTemp = PhotoImage(file="Screenshot 2022-02-01 114432.png")
        tampBut = Button(self.window, image=self.ImgTemp, highlightthickness=0)
        tampBut.grid(row=3, column=1 , rowspan=2)

        # canvasTeplota = Canvas(self.window, width=300, height=150)
        # self.Img = PhotoImage(file="Screenshot 2022-02-01 114432.png")
        # canvasTeplota.create_image(150, 207, image=self.Img)
        # quoteText = canvasTeplota.create_text(80, 50, text=f"Teplota : { round(self.data['temp'] - 273.1500 ,1) } C°", width=200,font=("Arial", 15, "bold"))
        # canvasTeplota.grid(row=1, column=1)

        canvasPocitovaTeplota = Canvas(self.window, width=300, height=60)
        canvasPocitovaTeplota.create_text(70, 50,text=f"Tlak : {self.data['pressure']}",width=200, font=("Arial", 15, "bold"))
        canvasPocitovaTeplota.grid(row=3, column=3)

        self.ImgPress = PhotoImage(file="index258.png")
        tampBut = Button(self.window, image=self.ImgPress, highlightthickness=0)
        tampBut.grid(row=4, column=3)


        canvasPocitovaTeplota = Canvas(self.window, width=300, height=60)
        canvasPocitovaTeplota.create_text(70, 50, text=f"Vlhkosť : {self.data['humidity']}", width=200,font=("Arial", 15, "bold"))
        canvasPocitovaTeplota.grid(row=3, column=4)

        self.ImgHum = PhotoImage(file="index147.png")
        tampBut = Button(self.window, image=self.ImgHum, highlightthickness=0)
        tampBut.grid(row=4, column=4)

    def zavrietOkno(self):
        #self.window.mainloop()
        self.window.destroy()

    def tlacitkoBack(self):
        buttSpat = Button( self.window , text="BACK" , highlightthickness=0 , command=self.zavrietOkno)
        buttSpat.grid(row=0,column=0)

