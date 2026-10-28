import threading


class VenderEntrada:
    def __init__(self, entradas):
        self.entradas = entradas
        self.lock = threading.Lock()

    def vender(self, comprador, cantidad):
        with self.lock:
            if cantidad <= self.entradas:
                self.entradas -= cantidad
                print(
                    f"{comprador} compra {cantidad} entrada(s). "
                    f"Quedan {self.entradas}."
                )
            else:
                print(
                    f"{comprador} quiere {cantidad} entrada(s), "
                    f"pero solo quedan {self.entradas}."
                )


compradores = [
    {"nombre": "Pepe Pérez", "nent": 2},
    {"nombre": "María Gómez", "nent": 3},
    {"nombre": "Sergio Dimas", "nent": 1},
    {"nombre": "Pedro Sanz", "nent": 2},
    {"nombre": "Abel Martín", "nent": 1},
]

vendedor = VenderEntrada(7)
hilos = []

for comprador in compradores:
    hilo = threading.Thread(
        target=vendedor.vender,
        args=(comprador["nombre"], comprador["nent"])
    )
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Entradas restantes: {vendedor.entradas}")