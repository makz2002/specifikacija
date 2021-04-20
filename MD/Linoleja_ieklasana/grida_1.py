import math

def gridas_izmaksa(cena, telpas_izmers):
    izmaksa = telpas_izmers * cena
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
    
    t_i = input("Ievadiet telpas izmēru: ")
    try:
        telpas_izmers = float(t_i)
    except ValueError:
        print("Jāievada skaitli! Ievadiet velreiz!")
        continue
    
    print("izmaksas: ")
    print(gridas_izmaksa(cena, telpas_izmers))
    print("\nVai Jūms ir jāizveido vel vienu aprēķinājumu?")
    print("Jā(J/j)                               Nē(N/n)")
    if not option(): break
print("Darbība pabeigta!")
    
    
        