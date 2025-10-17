# Programa para gestionar las notas de los estudiantes

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Salir")

def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return None
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            notas = []
            for i in range(3):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas.append(nota)
                try: #3
                    nota = float(input(f"Ingrese la nota {i+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        nota_valida = True
                    else:
                        print("error: ingresa el numero valido.")
                except ValueError:
                    print("ingresa el numero valido.")
                print(f"  Primeras dos notas: {est['notas'][:2]}") #4
        elif opcion == "5": #5
            if len(estudiantes) == 0:
                print("\n no hay estudiante registrado.")
            else:
                nombre_buscar = input("ingresa el nombre del estudiante buscado:")
                encontrado = False
                for est in estudiantes:
                    if est["nombre"].lower() == nombre_buscar.lower():
                        encontrado = True
                        print("\n" + "=" * 40 )
                        print(f"estudiantes: {est['nombre']}")
                        print(f"notas: {est['notas']}")
                        print(f"promedio: {est['promedio']:.2f}")
                        estado = "aprobado" if est["aprobado"] else "reprobado"
                        print(f"estado: {estado}")
                        print("=" * 40)
                        break
                if not encontrado:
                    print(f"nose encontro un estudiantes con ese nombre '{nombre_buscar}'.")

            promedio = calcular_promedio(notas)
            aprobado = promedio >= 6.0
            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }
            estudiantes.append(estudiante)
            print(f"\nEstudiante {nombre} agregado correctamente.")

        elif opcion == "2":
            print("\n=== LISTA DE ESTUDIANTES ===")
            for est in estudiantes:
                estado = "Aprobado" if est["aprobado"] else "Reprobado"
                print(f"{est['nombre']} - Promedio: {est['promedio']:.2f} - {estado}")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

main()
