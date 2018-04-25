# submission.py 

def zeitinSekunden(h, m, s):
    gesamt = 0
    gesamt += h*3600
    gesamt += m*60
    gesamt += s
    return gesamt

abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:01 correct"
t = abgabe.split(" ")

startzeit = t[0]
submissions = t[1]
bestezeit = "23:59:59"
besteruser = -1
b = 0

for x in range (2, len(t), 3):

    user = t[x]
    zeit = t[x+1]
    korrekt = t[x+2]

    print("Abgabe: ", user, zeit, korrekt)

    a = zeit.split(":")

    h = int(a[0])
    m = int(a[1])
    s = int(a[2])
    print(h, m, s)
    
    if(korrekt == "correct"):

        b = zeit.zeitinSekunden(h, m, s)
        a = 50000000
    
        if(a > b):
    
            a = b
            besteruser = user

