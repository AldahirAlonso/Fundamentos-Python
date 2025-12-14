def hotel():
    habitaciones = {"individual": 3, "doble": 2}
    while True:
        accion = input("¿Reservar o liberar? ")
        match accion:
            case "Reservar" | "reservar":
                print ("qué tipo de habitación quiere reservar")
                tipo = input("Tipo: ")
                if tipo in habitaciones and habitaciones[tipo] > 0:
                    habitaciones[tipo] -= 1
                    print(f"Habitación {tipo} reservada")
                else:
                    print("No disponible")
            case "Liberar" | "liberar":
                print ("que tipo de habitación quiere liberar")
                tipo = input("Tipo: ")
                if tipo in habitaciones:
                    habitaciones[tipo] += 1
                    print(f"Habitación {tipo} liberada")
            case "Salir" | "salir":
                break
            case _:
                print("Acción no reconocida")
        print("Estado:", habitaciones)

hotel()
