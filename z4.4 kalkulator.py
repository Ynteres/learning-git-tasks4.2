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

# Cztery funkcje -> add, subtract, multipy i devide 
# te 4 funkcje zostały umieszczone w pliku calculatorfunctions.py i zaimportowane do pliku głownego 
 
'''

def print_choice(option,x=0,y=0):
    if option == 1:
        a=logging.info("Dodaje - opcja %d , suma %s + %s" %(option, str(x),str(y)))
    elif option == 2:
        a=logging.info("Odejmuję - opcja %d , różnica %s - %s" %(option, str(x),str(y)))
    elif option == 3:
        a=logging.info("Mnożę - opcja %d , iloczyn %s * %s" %(option, str(x),str(y)))
    elif option == 4:
        a=logging.info("Dodaje - opcja %d , iloraz %s / %s" %(option, str(x),str(y)))
    return a
'''

def main():
    logging.basicConfig(level=logging.INFO)    #, filename="z4.4callog.log")

    print("Ktora operacje wybierasz -\n"
    "1. Dodawanie\n"
    "2. Odejmowanie\n"
    "3. Mnożenie\n"
    "4. Dzielenie\n") 
  
# odczyt wyboru dokonanego przez operatora  
    option = int(input("Wybierz operacje 1, 2, 3 lub 4 :")) 
    
    if option == 1:
        x = float(input("Podaj pierwszą liczbę: ")) 
        y = float(input("Podaj drugą liczbę: "))
        print_choice(option,x,y)
        print("Dodaję ",x, "+", y, "=", add(x, y)) 
    
    elif option == 2: 
        x = float(input("Podaj pierwszą liczbę: ")) 
        y = float(input("Podaj drugą liczbę: "))
        print_choice(option,x,y)
        print("Odejmuję ",x, "-", y, "=", "%.2f" % (subtract(x, y))) 
    
    elif option == 3: 
        x = float(input("Podaj pierwszą liczbę: ")) 
        y = float(input("Podaj drugą liczbę: "))
        print_choice(option,x,y)
        print("Mnożę ",x, "*", y, "=", multiply(x, y)) 
    
    elif option == 4: 
        x = float(input("Podaj pierwszą liczbę: ")) 
        y = float(input("Podaj drugą liczbę: "))
        print_choice(option,x,y)
        print("Dzielę",x, "/", y, "=", divide(x, y)) 
    else:
        print("Nie dokonałeś prawidłowego wyboru. Bywa. Podaj wybór 1-4") 

if __name__ == "__main__":
    main()
