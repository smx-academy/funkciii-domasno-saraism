'''Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, 
da se presmeta zbirot i da se ispecati dali zbirot e paren ili ne paren. Broevite da gi vnese korisnikot.'''

def zbir(x,y):
    v=x+y
    print('zbirot na vnesenite broevi e', v)
x=int(input('Vnesete broj x\n'))
y=int(input('Vnesete broj y\n'))
v=x+y
if v%2==0:
    print('Zbirot na broevite sto gi vnesovte e paren i e ednakov na', v)
else:
    print('Zbirot na broevite sto gi vnesovte e neparen i e ednakov na', v)
