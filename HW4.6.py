'''Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar, 
da go njade najdolgoto ime od lista, da go ispecati i da kaze od kolku parametri e sostaveno. 
Korisnikot da gi vnesuva iminjata'''

l=[]
def najdolgo_ime(l):
    return max (l, key=len)
x=int(input('Kolku pati ke se izvrsuva ciklusot?\n'))
for i in range(x):
    a=input('Vnesete ime\n')
    key=len(a)
    l.append(a)
print('Najdolgoto ime od listata e', najdolgo_ime(l), 'i ima', key, 'karakteri')