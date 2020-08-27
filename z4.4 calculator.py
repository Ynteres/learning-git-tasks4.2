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
def menu():
    print ("Podaj działanie, posługując się odpowiednią liczbą:\n"
    "1 - Dodawanie\n"
    "2 - Odejmownie\n"
    "3 - Mnożenie\n"
    "4 - Dzielenie\n")

def enternumber(prompt='podaj liczbę: '):
    while True:
        try:
            out=float(input())
        else:
            return out
