""" Stwórz funkcję, w której dodasz dwie liczby 
i wyświetl to na ekranie. Jak ją nazwiesz? 
Funkcję stworzysz z użyciem def. 
W ciele umieść operację i funkcję print."""

def sum_ab():
    a=0
    b=0
    c=0
    print("podaj liczbę A :")
    a = int(input())
    print("podaj liczbe B :")
    b = int(input())
    c = a+b
    print("suma liczb A=%d i B=%d to : %d" %(a,b,c))

sum_ab()

"""
test funkcji zakupy
"""
def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart
print("\n KOLEJNA FUNKCJA \n")
print(shopping())

"""
Jakiego typu jest None? Przetestuj to, wywołując 
funkcję type na rezultacie funkcji, która nic nie zwraca.
odp: <class 'NoneType'> 
"""
print(type(None))