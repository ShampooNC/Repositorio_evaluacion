def ingresar_datos_trabajador():
    nombre_trabajador = input("Ingresar nombre del trabajador: ")
    while not nombre_trabajador or len(nombre_trabajador) > 30:
        print("Ingresa el nombre del trabajador 'maximo 30 caracteres.'.")
        nombre_trabajador = input("Ingresa nombre del trabajador: ")

    sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
    while sueldo_base <= 0:

        sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))

    horas_extras = float(input("Ingrese el número de horas extras trabajadas en el mes: "))
    while horas_extras < 0:
        if horas_extras > 180:
            horas_extras = (horas_extras-180)*1.5


    return nombre_trabajador, sueldo_base, horas_extras

def calcular_liquidacion(sueldo_base, horas_extras):
    costo_hora_extra = 1500
    pago_horas_extras = horas_extras * costo_hora_extra
    total_ingresos = sueldo_base + pago_horas_extras
    descuento_fonasa = total_ingresos * 0.07
    descuento_fonasa = round(descuento_fonasa)
    descuento_afp = total_ingresos * 0.10
    descuento_afp = round(descuento_afp)
    sueldo_neto = total_ingresos - descuento_fonasa - descuento_afp
    return pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto

def mostrar_liquidacion(nombre_trabajador, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("\nLiquidación para el trabajador", nombre_trabajador)
    print(f"Sueldo base: ${sueldo_base:.2f}")
    print(f"Pago por horas extras: ${pago_horas_extras:.2f}")
    print(f"Total de ingresos: ${total_ingresos:.2f}")
    print(f"Descuento por FONASA: ${descuento_fonasa:.2f}")
    print(f"Descuento por AFP: ${descuento_afp:.2f}")
    print(f"Sueldo neto a pagar: ${sueldo_neto:.2f}")

def generar_archivo_liquidacion(nombre_trabajador, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    nombre_archivo = f"liquidacion_{nombre_trabajador}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Nombre del trabajador: {nombre_trabajador}\n")
        archivo.write(f"Sueldo base: ${sueldo_base:.2f}\n")
        archivo.write(f"Pago por horas extras: ${pago_horas_extras:.2f}\n")
        archivo.write(f"Total de ingresos: ${total_ingresos:.2f}\n")
        archivo.write(f"Descuento por FONASA: ${descuento_fonasa:.2f}\n")
        archivo.write(f"Descuento por AFP: ${descuento_afp:.2f}\n")
        archivo.write(f"Sueldo neto a pagar: ${sueldo_neto:.2f}\n")

if __name__ == "__main__":
    while True:
        nombre_trabajador, sueldo_base, horas_extras = ingresar_datos_trabajador()

        pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)

        mostrar_liquidacion(nombre_trabajador, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

        generar_archivo_liquidacion(nombre_trabajador, sueldo_base, pago_horas_extras, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)

        print(f"\nArchivo de liquidación generado: liquidacion_{nombre_trabajador}.txt\n")
        continuar = input("¿Desea calcular otra liquidación? (si/no): ")
        if continuar.lower() != "s":
            break
