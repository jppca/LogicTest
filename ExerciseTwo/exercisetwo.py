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

#Función para ingresar los casos de prueba que se desean determinar, en base a las especificaciones.

def icp():
    while True:
        b = ['B','C','A','D']
        aux = 0
        numi = ''
        numf = ''
        ei = ''
        ef = ''
        ryc = input('Ingrese el rango de años A-B:\n')

        for pos,char in enumerate(ryc):
            if(char == "-"):
                aux = pos
                break
            else:
                if(char.isdigit()):
                    numi += char

        for pos,char in enumerate(ryc):
            if(pos > aux):
                if(char.isdigit()):
                    numf += char
        
        for i in b:
            for pos,char in enumerate(ryc):
                if(pos == aux):
                    break
                else:
                    if( i == char):
                        ei += i

        for pos,char in enumerate(ryc):
            if(pos > aux):
                for i in b:
                    if( i == char):
                        ef += i
        if(ei == 'BC' and int(numi) > 753):
            print('Año ingresado no corresponde a la época de Roma.')
        elif(ef == 'BC' and int(numf) > 753):
            print('Año ingresado no corresponde a la época de Roma.')
        else:
            print(maxcara(yrom(int(numi),ei),yrom(int(numf),ef)))
            exit()

#Ejecución de icp()
#Para ejecutar las pruebas unitarias a las funciones comentar la siguiente línea. 

icp() 