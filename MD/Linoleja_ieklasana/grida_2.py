import math

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums):
    telpas_izmers = math.ceil(telpas_garums) * math.ceil(telpas_platums)
    izmaksa = telpas_izmers / linoleja_platums
    return izmaksa
    
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
    
while True:
    c = input("Ievadiet cenu: ")
    try:
        cena = float(c)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue
    
    l_p = input("Ievadiet linoleja platumu: ")
    try:
        linoleja_platums = float(l_p)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue
    
    t_p = input("Ievadiet telpas platumu: ")
    try:
        telpas_platums = float(t_p)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue
    
    t_g = input("Ievadiet telpas garumu: ")
    try:
        telpas_garums = float(t_g)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue
    
    print("izklājot garumā: ")
    print(gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums))
    print("izklājot platumā: ")
    print(gridas_izmaksa(cena, linoleja_platums, telpas_garums, telpas_platums))
    print("\nVai Jūms ir jāizveido vel vienu aprēķinājumu?")
    print("Jā(J/j)                               Nē(N/n)")
    if not option(): break
print("Darbība pabeigta!")
    
    
        