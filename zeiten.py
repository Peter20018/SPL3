# zeiten.py 

beginnZeit = input("Beginnzeit: ")
endeZeit = input("Endzeit: ")

beginn = beginnZeit.split(":")
print(beginn)

h = int(beginn[0])
m = int(beginn[1])
s = int(beginn[2])

print("Stunden: " , h)
print("Minuten: ", m)
print("Sekunden: ", s)