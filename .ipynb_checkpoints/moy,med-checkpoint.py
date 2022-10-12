def moyenne(l1):
    total = sum(l1)
    moy = total / len(l1)
    return moy

#print(moyenne([1,2,3,4,5,6]))

def médiane(l1): 
    if len(l1) % 2 == 1:
        med = l1[len(l1)//2]
    elif len(l1) % 2 == 0:
        med = (l1[len(l1)//2] - 1) + (l1[len(l1)//2]) / 2
    return med

# print(médiane([1,2,3,4,5,6])) 

def variance(l1):
    var = 0
    for i in range (len(l1)):
        var += (l1[i] - moyenne(l1))**2
    return var
# print(variance([1,2,3,4,5,6]))

def écartype(l1):
    éca = variance(l1)**0.5
    return éca
# print(écartype([1,2,3,4,5,6]))

    