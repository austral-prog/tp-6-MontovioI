# Listas a utilizar para los diferentes métodos
lista1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
lista2 =  ['Red', 'Green', 'White', 'Black']
lista3 =  []
lista4 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]

# Métodos
def remove_elements(lrem):
    if len(lrem)>0:
        del lrem[0]
    if len(lrem)>4:
         del lrem[4]
         del lrem[3]
    return lrem

def add_elements(ladd):
    ladd.insert(0, 'Pink')
    ladd.insert(len(ladd), 'Yellow')
    return ladd

def is_empty(lempty):
    if len(lempty)==0:
        return True
    else:
        return False

def check_lists(lcomp1, lcomp2):
    if len(lcomp1)>2 and len(lcomp2)>2:
        if lcomp1[2]==lcomp2[2]:
            return True
        else:
            return False

def list_of_lists(listadelistas):
    listaa=listadelistas[0][0:2]
    listab=listadelistas[1][1:4]
    listac=listadelistas[2][len(listadelistas[2])-2:len(listadelistas[2])]
    listad=[listaa,listab, listac]
    return listad

