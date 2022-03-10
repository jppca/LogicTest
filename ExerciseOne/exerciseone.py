# -- coding: utf-8 --
#Función que define un número par.

def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

#Función que establece reglas en base al número de filas y columnas para determinar la orientación final.
#En esta función se evalúa si n o m es par y cuál de ellos es mayor o menor o si hay una igualdad entre ambos.
#A partir de esto se determina la orientación final que se tendría tras un recorrido de caracol,
# que siempre partiría del punto (0,0) y que siempre giraría a la derecha hasta concluir el recorrido.

def rules(n,m):
    if par(n) and par(m) and n<=m:
        return "L"
    elif par(n) and par(m) and n>m:
        return "U"
    elif par(n) != True and par(m) != True and n<=m:
        return "R"
    elif par(n) != True and par(m) != True and n>m:
        return "D"
    elif par(n) != True and par(m) and n>m:
        return "U"
    elif par(n) != True and par(m) and n<m:
        return "R"
    elif par(n) and par(m) != True and n>m:
        return "D"
    elif par(n) and par(m) != True and n<m:
        return "L"