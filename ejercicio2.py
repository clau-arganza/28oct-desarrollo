import threading
import time
import random

sistemas = [
    "Propulsión",
    "Navegación",
    "Soporte vital",
    "Comunicaciones",
    "Combustible"
]

semaforo = threading.Semaphore(3)

# Cambia a True para simular un fallo.
forzar_error = False


def lanzar():
    print("\nTodos los sistemas preparados. ¡Lanzamiento!")


barrera = threading.Barrier(len(sistemas), action=lanzar)


def chequear(sistema):
    try:
        with semaforo:
            print(f"Iniciando chequeo: {sistema}")
            time.sleep(random.uniform(1, 3))

            if forzar_error and sistema == "Navegación":
                print(f"ERROR en {sistema}. Lanzamiento cancelado.")
                barrera.abort()
                return

            print(f"{sistema}: chequeo completado")

        # Liberamos el semáforo antes de esperar a los demás.
        barrera.wait()

    except threading.BrokenBarrierError:
        print(f"{sistema}: lanzamiento abortado")


hilos = []

for sistema in sistemas:
    hilo = threading.Thread(target=chequear, args=(sistema,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()