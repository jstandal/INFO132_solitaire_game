import random as rnd
import os.path

#Generer en random stokk for nytt spill
def genererSpill():
    sparSymbol = '\u2660'
    ruterSymbol = '\u2666'
    kløverSymbol = '\u2663'
    hjerterSymbol = '\u2665'
    tall = [7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    symbol = [sparSymbol, kløverSymbol, hjerterSymbol, ruterSymbol]
    kortstokk = []
    stokk1 = []
    stokk2 = []
    stokk3 = []
    stokk4 = []
    stokk5 = []
    stokk6 = []
    stokk7 = []
    stokk8 = []

    nyttspill = [stokk1, stokk2, stokk3, stokk4, stokk5, stokk6, stokk7, stokk8]

    for i in tall:
        for j in symbol:
            kortstokk.append([j, i])

    for i in nyttspill:
        if len(kortstokk) > 0:
            while len(i) <= 3:
                x = rnd.choice(kortstokk)
                i.append(x)
                kortstokk.remove(x)

    return nyttspill

#Skriver stokken for hver runde
def skriv_stokk(n):
    for i in n:

        if i == None:

            y = "--"
            return y
        elif i == []:

            z = "--"
            return z
        else:

            x = "".join(map(str, n[0]))
            return x

#Sjekker om det er gyldige trekk igjen
def gyldig(n):
    teller = 0
    for i in n:
        if i == None:
            continue
        for j in n:
            if j == None:
                continue
            elif i[1] == j[1] and i != j:
                teller += 1
    if teller > 0:
        return True
    else:
        return False

#Sjekker om input er gyldig
def inputValg():
    while True:
        input1 = input(":").upper()
        gyldiginput = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',"LAGRE"]

        if input1 == "LAGRE":
            return input1
        elif input1 in gyldiginput:
            return gyldiginput.index(input1)
        else:
            print("UGYLDIG INPUT! Velg bunke med bokstav fra A til H")

#Sjekker om spillet er vunnet eller tapt
def sjekkSpill(n):
    teller = 0
    for i in n:
        if i != []:
            teller += 1
    if teller > 0:
        print("Ingen flere mulig trekk. Du tapte!")
    else:
        print("Gratulerer, du vant!")

#Skriver ut hvor mange kort som er igjen i hver bunke
def skrivBunkestørrelse(n):
    lst = []
    for i in n:
        lst.append("   "+str(len(i))+"  ")
    return lst

#Lagrer spillet
def lagreSpill(n):
    dokument = open('dokument.txt','w')
    for i in n:
        for j in i:
            if j[0] == '\u2663':
                dokument.write('klover '+ str(j[1])+'-')
            elif j[0] == '\u2660':
                dokument.write('spar '+ str(j[1])+'-')
            elif j[0] == '\u2666':
                dokument.write('ruter '+ str(j[1])+'-')
            elif j[0] == '\u2665':
                dokument.write('hjerter '+ str(j[1])+'-')
            else:
                print(j)
        dokument.write('\n')
    dokument.close()

#Laster inn spillet
def lasteSpill():
    if os.path.exists('dokument.txt') == True:
        dokument = open('dokument.txt', 'r')
        lst = []
        for i in dokument:
            lst2 = []
            x = i.strip().split("-")
            for j in x:
                y = j.strip().split()
                if len(y)>0:
                    if y[0] == 'klover':
                        lst2.append(['\u2663',y[1]])
                    elif y[0] == 'spar':
                        lst2.append(['\u2660',y[1]])
                    elif y[0] == 'ruter':
                        lst2.append(['\u2666',y[1]])
                    elif y[0] == 'hjerter':
                        lst2.append(['\u2665',y[1]])
                    else:
                        print(j)
            lst.append(lst2)
        return lst
    else:
        print("Finner ingen lagrede filer.")


while True:
    print("--------------")
    print("1 - Nytt Spill")
    print("2 - Last spill")
    print("--------------")
    valg = input(":")

    if int(valg) == 1: spill = genererSpill()
    elif int(valg) == 2: spill = lasteSpill()
    else: print("Ugyldig input. Velg 1 for nytt spill, eller 2 for å laste inn lagret spill")

    fortsett = True
    lagret = False

    while fortsett == True:
        status = list(map(skriv_stokk, spill))
        status2 = []

        for i in status:
            if i == None:
                status2.append("--")
            else:
                status2.append(i)

        fortsett = gyldig(status)

        print("   A     B     C     D     E     F     G     H    ")
        print(status2)
        print(''.join(skrivBunkestørrelse(spill)))

        if fortsett == False: break
        print('Skriv "Lagre" for å lagre og avslutte spillet')
        print('Velg første bunke:')
        x = inputValg()

        if x == "LAGRE":
            lagreSpill(spill)
            lagret = True
            break

        print("Velg andre bunke")
        y = inputValg()

        try:
            if status[x][1] == status[y][1]:
                spill[x].remove(spill[x][0])
                spill[y].remove(spill[y][0])
            else:
                print("Verdiene er ulike! Prøv på nytt")
        except:
            print("Du har valgt en tom bunke! Prøv på nytt.")

    if lagret is True:
        print("Spill lagret.")
    else:
        sjekkSpill(spill)
    

