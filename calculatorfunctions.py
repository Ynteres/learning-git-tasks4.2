# Cztery funkcje -> add, subtract, multipy i devide  

def add(a, b): 
    return a + b 
  
def subtract(a, b): 
    return a - b 
  
def multiply(a, b): 
    return a * b 
  
def divide(a, b): 
    return a / b 

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