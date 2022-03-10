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

#Función para ingresar los casos de prueba que se desean determinar, en base a las especificaciones.          

def icp():
    result = []
    while True:
        try:
            t = int(input("Ingrese casos de prueba:\n"))
            if 1 <= t <=5000:
                for i in range(t):
                    print("Caso de prueba " + str(i))
                    n = int(input("Ingrese n:\n"))
                    if 1 <= n <= 10**9: 
                        m = int(input("Ingrese m:\n"))
                        if 1 <= m <= 10**9:  
                            result.append(rules(n,m))
                        else:
                            print("Error número m no válido.")
                            print("El número debe estar entre 1 y 10^9.")
                            exit()
                    else:
                        print("Error número n no válido.")
                        print("El número debe estar entre 1 y 10^9.")
                        exit()
                print("----Resultados----\n")
                for i in result:    
                    print(i)
                exit()
            else:
                print("Error número de casos de prueba no válido")
                print("El número debe estar entre 1 y 5000.")
        except ValueError:
                print("ATENCIÓN: Debe ingresar un número.")

#Ejecución de icp()
#Para ejecutar las pruebas unitarias a las funciones comentar la siguiente línea. 

icp()