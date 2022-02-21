import tkinter
import requests
from tkinter import *
from Hodinova import Hodinova
from Denna import Denna
from Aktualna import Aktualna
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

#=================FUNKCIE PRE ZOBRAZENIE OKIEN==========================
def zobrazAktualna():
    #aktualna.oknoNaTeplotu()
    aktualna.zobraz_okno()
    aktualna.zobrazData()
    aktualna.tlacitkoBack()
    #aktualna.vypisData()


def zobrazDenna():
    denna.zobraz_okno()
    denna.dniTyzdna(1)
    denna.tlacitkoBack()
    denna.grafTeplot()
    denna.grafDazda()

def zobrazHod():
    hodinova.zobraz_okno()
    hodinova.hodinyDna()
    hodinova.tlacitkoBack()
    hodinova.grafTeplot()
    hodinova.grafOblacnosti()


#=================POMOCNE FUNKCIE ============================================
def konrolaSuradnic():
    savingGPS()
    try:
        print(f"latuitude {int(latitude.get())}" )
        print(f"lontitude {int(longtitude.get())}" )

        if (int(latitude.get()) < 180 and int(latitude.get()) > -180):
            if (int(longtitude.get()) < 90 and int(longtitude.get()) > -90):
                weatherParams["lat"] = int(latitude.get())
                weatherParams["lon"] = int(longtitude.get())
                oknoSuradnic.destroy()
                vytvorUvodneOkno()
            else:
                messagebox.showerror(title="ERROR", message="Nespravne zadaná šírka")
        else:
            messagebox.showerror(title="ERROR", message="Nespravne zadaná výška ")
    except ValueError:
        messagebox.showerror(title="", message="Nenechávaj prazdne miesta")


def savingGPS():
    lonEntrTxt = longtitude.get()
    latEntrTxt = latitude.get()
    if lonEntrTxt == "" or latEntrTxt =="" :
        print("Nenechávaj prazdne miesta")
    else:
        with open("GPS.txt" ,mode="w") as dataFile:
            dataFile.write(f"{lonEntrTxt} {latEntrTxt}")
            #vyska.delete(0,END)
            #sirka.delete(0,END)


# ===============================VYTVORENIE A UPRAVA UVODNEHO OKNA======================
def vytvorUvodneOkno():

    uvodne_oko = Tk()
    uvodne_oko.title("Uvodné okno")
    uvodne_oko.config(padx=20, pady=20)

    def oknoDestroy():
        uvodne_oko.destroy()

    buttonExit = Button(text="EXIT", highlightthickness=0, command=oknoDestroy, pady=10, padx=10)
    buttonExit.grid(row=0, column=3)

    imgAktu = PhotoImage(file="images.png")
    aktual_Button = Button(image=imgAktu, highlightthickness=0, command=zobrazAktualna)
    aktual_Button.grid(row=2, column=0)

    imgDenna = PhotoImage(file="images12.png")
    denna_Button = Button(image=imgDenna, highlightthickness=0, command=zobrazDenna)
    denna_Button.grid(row=2, column=1)

    imgHod = PhotoImage(file="images1234.png")
    hodin_Button = Button(image=imgHod, highlightthickness=0, command=zobrazHod)
    hodin_Button.grid(row=2, column=2)

    labelAktualna = Label(text="Aktuálna", font=("Arial", 20, "bold"))
    labelAktualna.grid(row=1, column=0)

    labelDenna = Label(text="Denná", font=("Arial", 20, "bold"))
    labelDenna.grid(row=1, column=1)

    labelHodinova = Label(text="Hodinová", font=("Arial", 20, "bold"))
    labelHodinova.grid(row=1, column=2)

    # sirkaLabel = Label(text=f"Zemepisná šírka (lat) 48 je : {weatherParams['lat']}" , font=("Arial" , 13))
    # #print("tutu: " + str(weatherParams))
    # sirkaLabel.grid(row=3,column=1)
    #
    # vyskaLabael = Label(text=f"Zemepisná výška je (lon) 18 : {weatherParams['lon']}" , font=("Arial" , 13))
    # vyskaLabael.grid(row=4,column=1)

    # Img = PhotoImage(file="Screenshot 2022-02-01 114432.png")
    # tampBut = Button(image=Img, highlightthickness=0)
    # tampBut.grid(row=0, column=3)

    uvodne_oko.mainloop()

#=============ZISKANIE DAT POMOCOU REQ==========================
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = '378d969c0481b240225a376c51d6f839'


#ošetrit viacrozmerny string
with open("GPS.txt") as file:
    datatxt = file.read()
gps = datatxt.split()
print(f"gps su : {gps}")
weatherParams = {
    "lat" : gps[0] ,
    "lon" : gps[1] ,
    "appid" : api_key
}

print(f" lat 48 je : {weatherParams['lat']}")
print(f" laon 18 je : {weatherParams['lon']}")

response = requests.get(OWN_Endpoint , params= weatherParams)
print(response)
#data = response.json()
from data import data1
data = data1
#print(data)

#=============ROZDELENIE DAT==============
hodinoveData = data["hourly"]
denneData = data["daily"]
aktualne = data["current"]

#=============VYTVORENIE OBJEKTOV JEDNOTLIVYCH PREDPOVEDI==============
aktualna = Aktualna(aktualne)
denna = Denna(denneData)
#denna.zobraz_okno()
hodinova = Hodinova(hodinoveData)
#hodinova.zobraz_okno()

#=============VYTVORENIE OKNA SURADNIC=========================
oknoSuradnic = Tk()
oknoSuradnic.title("Miesto predpovede")
oknoSuradnic.config(pady=20,padx=20)

vyskaLabael = Label(text="Zadaj Zemepisnú širku oblasti (lat) 48:")
vyskaLabael.grid(row=1,column=1)

sirkaLabel = Label(text="Zadaj Zemepisnú dĺžku oblasti (lon) 18:")
sirkaLabel.grid(row=2,column=1)

longtitude= Entry(width=50)
longtitude.insert(END, f"{gps[0]}")
longtitude.grid(row=1, column=2)
longtitude.focus()

latitude= Entry(width=50)
latitude.insert(END, f"{gps[1]}")
latitude.grid(row=2, column=2)
latitude.focus()

hladajButton = Button(text="Hladaj" , highlightthickness=0 , command= konrolaSuradnic )
hladajButton.grid(row=3,column=1)

oknoSuradnic.mainloop()


#canvas = Canvas(width=800,height=200)
#canvas.grid(row=0,column=0)




# df= DataFrame(grafData , columns= ['Teplota' , 'datumDna'])
# print(df)
#
# data2 = {'Datum': [7.2,8.2,9.2,10.2,11.2,12.2,13.2,14.2,15.2,16.2],
#          'Teplota_dni': [20,22,19,21,15,14,10,15,25,25]
#        }
# df2 = DataFrame(data2,columns=['Datum','Teplota_dni'])
# print (df2)
#
# figure2 = plt.Figure(figsize=(5,4) , dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2,uvodne_oko)
# line2.get_tk_widget().grid(row=1,column=2)
# df2 = df2[['Datum' , 'Teplota_dni']].groupby('Datum').sum()
# df2.plot(kind="line" , legend=True , ax = ax2 ,color='r' , marker = 'x' , fontsize=10)
# ax2.set_title('Teplota_dni vs Datum')

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
# plt.show()



