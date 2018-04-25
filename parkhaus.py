# parkhaus.py 
# Angabe für das Beispiel: siehe Moodle

a = 0;

print("Linienbus Simulator 2018!")

haltestellen = input("Wie viele Haltestellen gibt es? ")

haltestelle = int(haltestellen)

i = 0
while(i < haltestelle):
    i= i + 1
    y = a
    print("Sie sind an der Haltestelle " , i , ". Wie viele Personen steigen ein?")
    einsteiger = input()
    person = int(einsteiger)

    print("Wie viele Personen steigen aus?")
    aussteiger = input()
    draußen = int(aussteiger)

    a = a + person
    a = a - draußen

    print("Es sind zurzeit", a ," Personen im Bus")
    if(a > 60):

        print("Hallo steigen sie bitte aus, die maximale Anzahl an Passagieren ist überschritten!!")
        u = a - 60

        print("Es dürfen ", u ," Personen nicht mitfahren.")
        a = 60
    if(a < 0):
        i = i - 1
        print("Achtung! Es sind zurzeit ", y ," Personen im Bus!")
        a = y
    
print("Die Anzahl der eingestiegenen Personen beträgt " , a)