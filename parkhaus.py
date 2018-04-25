# parkhaus.py 
# Angabe für das Beispiel: siehe Moodle

a = 0;

print("Linienbus Simulator 2018!")

haltestellen = input("Wie viele Haltestellen gibt es? ")

haltestelle = int(haltestellen)

for i in range(1,haltestelle+1):

    print("Sie sind an der Haltestelle " , i , ". Wie viele Personen steigen ein?")
    einsteiger = input()
    person = int(einsteiger)

    print("Wie viele Personen steigen aus?")
    aussteiger = input()
    draußen = int(aussteiger)

    a = a + person
    a = a - draußen

print("Die Anzahl der eingestiegenen Personen beträgt " , a)