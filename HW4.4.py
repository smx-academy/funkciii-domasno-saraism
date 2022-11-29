'''Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri, 
da presmetuvaat plostinata i perimetarot na pravoagolnik. 
Korisnikot da gi vnesuva broevite i korisnikot da izbere koja presmetka da se izvrsi. DA NE SE IZVRSUVAAT DVETE'''

def triagolnik(a,b):
    plostina=a*b
    perimetar=2*a+2*b   

a=int(input('Vnesete broj\n'))
b=int(input('Vnesete broj\n'))
plostina=a*b
perimetar=2*a+2*b 
f=input('Koja funkicja sakate da ja presmetate, plostina ili permetar?\n')
if f=='plostina':
    print('Plostinata na triagolnikot e', plostina)
elif f=='perimetar':
    print('Perimetarot na triagolnikot e', perimetar)

triagolnik(a,b)