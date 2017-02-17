svar = 0
while svar == 0:
    print("1. Bæta í skrána")
    print("2. Birta skrána í heild sinni")
    print("3. Birta upplýsingar um ákveðið dýr eftir nafni þess")
    print("4. Hætta")
    val = input("Hvaða vilt þú gera? ")
    if val == "1":
        nafn = input("Hvað er nafnið eiganda? ")
        dyr = input("Hvað er nafn gæludýrsins? ")
        tegund = input("Hvað er tegund dýrsins? ")
        skra = open("skra.txt", "a")
        skra.write(nafn)
        skra.write(",")
        skra.write(dyr)
        skra.write(",")
        skra.write(tegund)
        skra.write(";")
        skra.close()

    elif val == "2":
        skra = open("skra.txt", "r")
        dyraskra = skra.read().split(";")
        skra.close()
        for i in dyraskra:
            print(i)
            print("\n")

    elif val == "3":
        skra = open("skra.txt", "r")
        dyraskra = skra.read().split(";")
        skra.close()
        eigandi = input("Hvað er nafn eiganda dýrsins? ")
        teljari = 0
        for i in dyraskra:
            faersla = i.split(",")
            if faersla[0] == eigandi:
                print("Nafn dýrsins:",faersla[1])
                print("Tegund dýrsins:",faersla[2])
            else:
                teljari = teljari+1

    elif val == "4":
        break