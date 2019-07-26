# Cuota mensual por prestamo de un banco

respuesta = "si"

while respuesta == 'si':

    print("____________________________________________________________")
    dinero_total = float(
        input("¿Cuanto dinero necesita en millones? ")) * 1000000
    tasa_prestamo = float(
        input("¿Cuanto porcentaje puede prestarle el banco? "))
    tasa_interes = float(
        input("¿cual es la tasa de interes anual de su banco? ")) / 1200
    dinero_prestado = (dinero_total * tasa_prestamo) / 100
    año = int(input("¿A cuantos años desea su prestamo? "))
    meses = año * 12
    cont = 0
    necesita = dinero_total - dinero_prestado
    mensual = dinero_prestado / meses
    costo_fijo = 0
    luego = dinero_prestado

    print("____________________________________________________________")

    print("El dinero prestado fue de: ", int(dinero_prestado))

    print("____________________________________________________________")

    print("El dinero que necesita de manera exterior es de: ", int(necesita))

    print("____________________________________________________________")

    print("Pago mensual sin tasa fija\n")

    for cuota_mensual in range(1, (meses + 1)):
        cont += 1
        actual = mensual + (dinero_prestado * tasa_interes)
        print(cont, "- ", int(actual))
        dinero_prestado = dinero_prestado - mensual
        costo_fijo += actual

    print("____________________________________________________________")

    print("El pago a tasa fija es de ", int(costo_fijo / meses))

    print("____________________________________________________________")

    print("El dinero pagado fue de: ", int(costo_fijo))

    print("____________________________________________________________")

    print("El dinero en interes fue de: ", (int(costo_fijo) - int(luego)))

    print("____________________________________________________________")
    print("____________________________________________________________")

    respuesta = (input("¿Desea continuar con otras opciones? < si - no>    "))

print("\nSaliste")
