'''Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata'''

l=[]
def lista(l):
    l=sum/len
x=int(input('Kolku broevi ke vnesete?\n'))
for n in range(x):
    y=int(input('Vnesete broj\n'))
    l.append(y)

prosek=sum(l)/len(l)
print(prosek)