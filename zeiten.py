# zeiten.py 

def zeitinSekunden(h, m, s):
    gesamt = 0
    gesamt += h*3600
    gesamt += m*60
    gesamt += s
    return gesamt


beginnZeit = input("Beginnzeit: ")
endeZeit = input("Endzeit: ")

beginn = beginnZeit.split(":")
print(beginn)

ende = endeZeit.split(":")
print(ende)

# Start 
h = int(beginn[0])
m = int(beginn[1])
s = int(beginn[2])

# Ende
a = int(ende[0])
b = int(ende[1])
c = int(ende[2])
print("Stunden: " , h)
print("Minuten: ", m)
print("Sekunden: ", s)

beginnSekunden = zeitinSekunden(h, m, s)
endeSekunden = zeitinSekunden(a, b, c)

differenzSekunden = endeSekunden - beginnSekunden
print("Differenz der Sekunden: ",differenzSekunden)