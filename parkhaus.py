# parkhaus.py 
# Angabe für das Beispiel: siehe Moodle

a = 0;

print("Linienbus Simulator 2018!")

haltestellen = input("Wie viele Haltestellen gibt es? ")

haltestelle = int(haltestellen)

for i in range(1,haltestelle+1):

    print("Sie sind an der Haltestelle " , i , ". Wie viele Personen steigen ein?")
    personen = input()
    person = int(personen)
    a = a + person
print("Die Anzahl der eingestiegenen Personen beträgt " , a)