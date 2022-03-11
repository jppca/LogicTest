# -- coding: utf-8 --
#Función encargada de retornar el año en base a los años de la fundación de la antigua Roma.
# 753 a.u.c - 1 BC
# 754 a.u.c - 1 DC

def yrom(a,e):
    if(e == "BC"):
        if (a == 753):
            return 1 
        else:
            return 753 - a
    else:
        return a + 753

#Función encargada de retornar el equivalente del número de año (arábigo) en número romano.
 
def convrom(ar):
    numroman = '' 
    numa_numr = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    while ar > 0:
        for i,r in numa_numr: 
            while ar >= i:
                numroman += r
                ar -= i

    return numroman 

#Función encargada de retornar el máximo de caracteres necesarios, tomando como entrada el rango de los años.

def maxcara(numi,numf):
    max = 0
    aux = 0
    
    for i in range(numi,numf+1):
        aux = len(convrom(i))
        if(aux > max):
            max = aux
    
    return max