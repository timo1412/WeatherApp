from data import Data
from suradnice import Suradnice
from uvodneOkno import UvodneOkno
#=================POMOCNE FUNKCIE ============================================

#


suradnice = Suradnice()
suradnice.oknoSuradnic()
gps = suradnice.getSuradnice()
print(f" Suradnice su {gps[0]} , {gps[1]}")

data = Data(paGps=gps)
weatherData = data.ziskajData()

uvodneOkno = UvodneOkno(paData=weatherData)
uvodneOkno.rozdelData()
uvodneOkno.vytvorPredpovede()

uvodneOkno.vytvorUvodneOkno()
#print(weatherData)



