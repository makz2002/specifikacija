def pasuti_tkreklus(skaits, apdruka, piegade):
    cena = skaits * apdruka
    if cena < 50 and piegade is True:
        cena += 15
    elif cena > 100:
        cena = cena * 0.95
    elif (cena < 50 and piegade is False) or cena >= 50:
        cena = cena
    return cena
    
def option():
    opt = input()
    while True:
        if opt == "J" or opt == "j":
            return True
        elif opt == "N" or opt == "n":
            return False
        else:
            print("Jāievada J/j vai N/n!")
            return option()
    
def teksts_sk():
    txt = input("Vai uz krekla ir vajadzīgs teksts? (J/j vai N/n) ")
    while True:
        if txt == "J" or txt == "j":
            return True
        elif txt == "N" or txt == "n":
            return False
        else:
            print("Jāievada J/j vai N/n!")
            return teksts_sk()
            
def zime_sk():
    z = input("Vai uz krekla ir vajadzīga zīme? (J/j vai N/n) ")
    while True:
        if z == "J" or z == "j":
            return True
        elif z == "N" or z == "n":
            return False
        else:
            print("Jāievada J/j vai N/n!")
            return zime_sk()

def foto_sk():
    f = input("Vai uz krekla ir vajadzīgs foto? (J/j vai N/n) ")
    while True:
        if f == "J" or f == "j":
            return True
        elif f == "N" or f == "n":
            return False
        else:
            print("Jāievada J/j vai N/n!")
            return foto_sk()

def piegade_sk():
    p = input("Vai Jūsu pasūtījumu ir jāpiegādā? (J/j vai N/n) ")
    while True:
        if p == "J" or p == "j":
            return True
        elif p == "N" or p == "n":
            return False
        else:
            print("Jāievada J/j vai N/n!")
            return piegade_sk()
            
while True:
    s = input("Ievadiet kreklu skaitu: ")
    try:
        skaits = int(s)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue

    if teksts_sk() is True:
        teksts = 5
    else:
        teksts = 0
        
    if zime_sk() is True:
        zime = 7
    else:
        zime = 0
        
    if foto_sk() is True:
        foto = 20
    else:
        foto = 0
        
    if piegade_sk() is True:
        pieg = True
    else:
        pieg = False    
        
    apdruka = teksts + zime + foto
    piegade = pieg

    print("Cena: ")
    print(pasuti_tkreklus(skaits, apdruka, piegade))
    print("\nVai Jūs vēlāties aprēķināt cenu vel vienam pasūtījumam?")
    print("Jā(J/j)                                         Nē(N/n)")
    if not option(): break
print("Darbība pabeigta")