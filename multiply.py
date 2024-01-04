import random
import os
from colorama import Fore, Style, init

init(autoreset=True)
debug = False

def mostrar_mensaje_bienvenida(nombre):
    print()
    print(" /$$      /$$ /$$   /$$ /$$       /$$$$$$$$ /$$$$$$ /$$$$$$$  /$$       /$$     /$$")
    print("| $$$    /$$$| $$  | $$| $$      |__  $$__/|_  $$_/| $$__  $$| $$      |  $$   /$$/")
    print("| $$$$  /$$$$| $$  | $$| $$         | $$     | $$  | $$  \ $$| $$       \  $$ /$$/ ")
    print("| $$ $$/$$ $$| $$  | $$| $$         | $$     | $$  | $$$$$$$/| $$        \  $$$$/  ")
    print("| $$  $$$| $$| $$  | $$| $$         | $$     | $$  | $$____/ | $$         \  $$/   ")
    print("| $$\  $ | $$| $$  | $$| $$         | $$     | $$  | $$      | $$          | $$    ")
    print("| $$ \/  | $$|  $$$$$$/| $$$$$$$$   | $$    /$$$$$$| $$      | $$$$$$$$    | $$    ")
    print("|__/     |__/ \______/ |________/   |__/   |______/|__/      |________/    |__/    ")
    print()
    print(Fore.MAGENTA + f"Bienvenido(a), {nombre}!" + Style.RESET_ALL)

def mostrar_menu():
    print(Fore.CYAN + "\n¿Qué tabla de multiplicar quieres trabajar? Elige un número del 1 al 10:" + Style.RESET_ALL)
    print(Fore.CYAN + "Pulsa 'x' para salir." + Style.RESET_ALL)

def obtener_nivel_dificultad():
    return int(input(Fore.CYAN + "\nElige el nivel de dificultad [0-4]: " + Style.RESET_ALL))

def imprimir_corazones(errores_permitidos):
    print(Fore.RED + "❤️ " * errores_permitidos + Style.RESET_ALL)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def preguntar_operaciones(tabla, modo):
    if modo == 'a':
        multiplicadores = random.sample(range(1, 11), 10)
    else:
        multiplicadores = list(range(1, 11))
    
    operaciones = [(tabla, multiplicador) for multiplicador in multiplicadores]
    return operaciones

def jugar_tabla(tabla, errores_permitidos, modo):
    operaciones = preguntar_operaciones(tabla, modo)
    operaciones_fallidas = []
    contador_preguntas = 0
    contador_errores = 0
    
    for multiplicador in operaciones:
        contador_preguntas += 1
        resultado_correcto = tabla * multiplicador[1]

        pregunta = Fore.YELLOW + f"{multiplicador[0]} x {multiplicador[1]} = " + Style.RESET_ALL
        respuesta_usuario = input(pregunta)
        
        while not respuesta_usuario.isdigit():
            print(Fore.RED + "No has introducido un número válido." + Style.RESET_ALL)
            respuesta_usuario = input(pregunta)

        respuesta_usuario = int(respuesta_usuario)

        if respuesta_usuario != resultado_correcto:
            errores_permitidos -= 1
            contador_errores += 1

            operaciones_fallidas.append(f"{multiplicador[0]} x {multiplicador[1]}")

            print(Fore.RED + "Incorrecto!\n" + Style.RESET_ALL)
            print()
            
            if errores_permitidos == 0:
                print(Fore.RED + "\nGame Over. Has agotado todos los intentos." + Style.RESET_ALL)
                print()
                print(Fore.YELLOW + f"Puntuación: {(contador_preguntas) - (contador_errores)}/10" + Style.RESET_ALL)
                
                if debug == True:
                    # Bloque control
                    print("Preguntas totales: ", contador_preguntas)
                    print("Errores totales: ", contador_errores)
                    print("Longitud de operaciones totales: ", len(operaciones))
                    print("Longitud de operaciones fallidas: ", len(operaciones_fallidas))
                    # Bloque control

                return operaciones_fallidas
        else:
            print(Fore.GREEN + "¡Correcto!\n" + Style.RESET_ALL)

        imprimir_corazones(errores_permitidos)
    
    print(Fore.GREEN + "\n¡Enhorabuena! Has completado la tabla." + Style.RESET_ALL)
    print(Fore.GREEN + f"Puntuación: {len(operaciones) - len(operaciones_fallidas)}/{len(operaciones)}" + Style.RESET_ALL)
    
    if debug == True:
        # Bloque control
        print("Preguntas totales: ", contador_preguntas)
        print("Errores totales: ", contador_errores)
        print("Longitud de operaciones totales: ", len(operaciones))
        print("Longitud de operaciones fallidas: ", len(operaciones_fallidas))
        print(f"Puntuación en base a la longitud de cadenas: {len(operaciones) - len(operaciones_fallidas)}/{len(operaciones)}")
        # Bloque control

    if operaciones_fallidas:
        print(Fore.RED + f"\n{name}, has fallado en las siguientes operaciones:" + Style.RESET_ALL)
        for operacion in operaciones_fallidas:
            print(Fore.RED + f" - {operacion}" + Style.RESET_ALL)
    
    return None

# Programa principal
name = "Vega"
mostrar_mensaje_bienvenida(name)

while True:
    print("\nQuieres que te pregunte aleatoriamente u ordenadamente?")
    modo = input("Pulsa 'a' para aleatoria u 'o' para ordenada: ").lower()
    
    if modo not in ['a', 'o']:
        print(Fore.RED + "Opción no válida. Debes elegir 'a' o 'o'." + Style.RESET_ALL)
        continue

    mostrar_menu()
    opcion = input()
    
    if opcion.lower() == 'x':
        break
    
    try:
        tabla = int(opcion)
        if 1 <= tabla <= 10:
            nivel = obtener_nivel_dificultad()
            errores_permitidos = 5 - nivel
            
            limpiar_pantalla()
            mostrar_mensaje_bienvenida(name)
            imprimir_corazones(errores_permitidos)
            
            resultado = jugar_tabla(tabla, errores_permitidos, modo)
            
            if resultado is not None:
                continue
        else:
            print(Fore.RED + "\nPor favor, elige un número del 1 al 10." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "\nEntrada no válida. Por favor, elige un número del 1 al 10 o 'x' para salir." + Style.RESET_ALL)
