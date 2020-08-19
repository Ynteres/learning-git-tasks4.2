# 4.2 Argumenty funkcji
""" 
FUNKCJA Z ZAKUPAMI
Wyobraź sobie, że zabrakło Ci jeszcze dwóch rzeczy 
i znowu musisz wyskoczyć do sklepu. 
Zmodyfikuj listę zakupów wpisując
 „chusteczki” i “papier toaletowy”, a następnie wywołaj funkcję.
"""

def shopping():
    a=input()
    b=input()
    shopping_items = [
        a,
        b,
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

print(shopping())