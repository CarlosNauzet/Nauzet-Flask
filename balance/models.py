"""
Un movimiento debe tener:

1. Fecha
2. COncepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""


import csv

from . import RUTA_FICHERO

class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad


class ListaMovimientos:
    """
    Almacenar y gestionar la lista con todos los movimientos
    """
    def __init__(self):
        self.lista_movimientos = []
    
    def leer_desde_archivo(self):
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                self.lista_movimientos.append(fila)