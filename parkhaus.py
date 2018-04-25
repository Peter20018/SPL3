# parkhaus.py 
# Angabe für das Beispiel: siehe Moodle

print("Linienbus Simulator 2018!")

haltestellen = input("Wie viele Haltestellen gibt es? ")

haltestelle = int(haltestellen)

for i in range(0,haltestelle):

    personen = input("Sie sind an der Haltestelle " ,i, ". Wie viele Personen steigen ein?")
    person = int(personen)

    i = i + person