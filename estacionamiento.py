def estacionamiento(num_carros):
    # Lugares de estacionamiento
    lugar_B = list(range(1, num_carros + 1)) 
    lugar_C = []  
    lugar_A = []  

    def imprimir_lugares():
        print(f"B: {lugar_B}")
        print(f"C: {lugar_C}")
        print(f"A: {lugar_A}")

    def pasar_a_c():
        if len(lugar_C) == 0:
            carro = lugar_B.pop(0)
            lugar_C.append(carro)
            print(f"Carro {carro} movido de B a C.")
            imprimir_lugares()
        else:
            print("No se puede mover a C, espacio ocupado.")

    def pasar_a_a():
        if len(lugar_C) > 0:
            carro = lugar_C.pop()
            lugar_A.append(carro)
            print(f"Carro {carro} movido de C a A.")
            lugar_A.sort()
            imprimir_lugares()
        else:
            print("No hay carros en C para mover a A.")
    while True:
        print("\nMenu:")
        print("1. Mover carro de B a C.")
        print("2. Mover carro de C a A.")
        print("3. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pasar_a_c()
        elif opcion == "2":
            pasar_a_a()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
if __name__ == "__main__":
    try:
        num_carros = int(input("Ingrese la cantidad de carros para B: "))
        estacionamiento(num_carros)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
