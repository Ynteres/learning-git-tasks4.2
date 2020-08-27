# zadanie z funkcją sprawdzajacą czy dany wyraz jest palindromem a funkcja zwraca prawdę lub fałsz

'''
The reverse() is an inbuilt method in Python programming language that reverses objects of list in place. Returns: The reverse() method does not return any value but reverse the given object from the list
The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator
'''

def palindrome(txt): 
    rtxt = ''.join(reversed(txt))
    if txt == rtxt: 
        return True
    return False
  
# main pgm 
txt = input()
t = palindrome(txt) 
  
if (t): 
    print("t :%s, Tak to jest palindrom" %(t)) 
else: 
    print("t :%s, Przykro mi ale to nie jest palindrom" %(t)) 