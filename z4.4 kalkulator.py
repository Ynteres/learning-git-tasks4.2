'''
Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty 
(np. Dodaję 1 i 3).

Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami, 
przewidujemy poprawne uzupełnienie.
'''
import logging
from calculatorfunctions import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="z4.4callog.log")

# Cztery funkcje -> add, subtract, multipy i devide 
# te 4 funkcje zostały umieszczone w pliku calculatorfunctions.py i zaimportowane do pliku głownego 
'''
def add(a, b): 
    return a + b 
  
def subtract(a, b): 
    return a - b 
  
def multiply(a, b): 
    return a * b 
  
def divide(a, b): 
    return a / b 
'''

def main():
    print("Ktora operacje wybierasz -\n"
    "1. Dodawanie\n"
    "2. Odejmowanie\n"
    "3. Mnożenie\n"
    "4. Dzielenie\n") 
  
# odczyt wyboru dokonanego przez operatora  
    option = int(input("Wybierz operacje 1, 2, 3 lub 4 :")) 
# odczyt cyfr podanych przez operatora  
    x = float(input("Podaj pierwszą liczbę: ")) 
    y = float(input("Podaj drugą liczbę: ")) 
  
    if option == 1: 
        print("Dodaję ",x, "+", y, "=", add(x, y)) 
    
    elif option == 2: 
        print("Odejmuję ",x, "-", y, "=", "%.2f" % (subtract(x, y))) 
    
    elif option == 3: 
        print("Mnożę ",x, "*", y, "=", multiply(x, y)) 
    
    elif option == 4: 
        print("Dzielę",x, "/", y, "=", divide(x, y)) 
    else: 
        print("Nie dokonałeś prawidłowego wyboru") 

if __name__ == "__main__":
    main()