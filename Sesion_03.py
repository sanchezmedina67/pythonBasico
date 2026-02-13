# Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:",i)

resultado = 0
for i in mi_lista:
    resultado+= i

    print(f"El resultado de la suma de mi lista es: {resultado}")
 
    for i in range(2,9):
        print(i)

    mi_lista_2 = ["Lunes","martes","miercoles","jueves","viernes"]

    for i in mi_lista_2:
        print("Los dias de la semana son: ",i)
        print(f"Feliz(i)!")

        #While loop
        i = 0

    while i < 5:
        if i == 3:
            continue
        print(i)
        if i ==4:
            break

        else:
            print("i es ahora mayor o igual a 5")

            # Practica 2 
            # Dada la lista mi_lista_ = ["Lunes","martes","miercoles","jueves","viernes"]
            # Imprime cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
            # Pista: Usa los dos tipos loop while y for en el mimo programa para lograrlo
            # Resultado:
            # Martes
            # Miercoles
            # Jueves
            # Viernes
            # Martes
            # Miercoles
            # Jueves
            # Viernes
            # Martes
            # Mircoles
            # Jueves
            # Viernes
             