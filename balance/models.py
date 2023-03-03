"""
Un movimiento debe tener:

1. Fecha
2. COncepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""


import csv
from datetime import date

from . import RUTA_FICHERO

CLAVES_IGNORADAS = ['errores']

class Movimiento:
    def __init__(self, dic_datos):
        self.errores = []

        fecha = dic_datos['fecha']
        concepto = dic_datos['concepto']
        tipo = dic_datos['tipo']
        cantidad = dic_datos['cantidad']

        try:
            self.fecha = date.fromisoformat(fecha)
            hoy = date.today()
            if self.fecha > hoy:
                self.errores.append("La fecha no puede ser futura")
                self.fecha = hoy
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0
    
    def __str__(self):
        if self.fecha is None:
            fecha = "---"
        else:
            fecha = self.fecha
        return f'{self.fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}'
    
    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    """
    Almacenar y gestionar la lista con todos los movimientos
    """
    def __init__(self):
        self.movimientos = []
    
    def leer_desde_archivo(self):
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                mov = Movimiento(fila)
                self.movimientos.append(mov)

    def agregar(self, movimiento):
        """
        Agrega el movimiento a la lista y actualiza el archivo CSV.
        """
        if not isinstance(movimiento, Movimiento):
            raise ValueError("No puedes agregar nada que no sea un movimiento")
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        """
        Actualiza el arcvhivo CSV con los movmientos que hay en la lista de movimientos.

        1. Vacía el archivo CSV
        2. Escribe la línea de cabecera con el nombre de los campos
        3. Escribe los movimentos uno a uno en el archivo CSV
        """
        with open('RUTA_FICHERO', 'w') as csvfile:
            fieldnames = list(self.movimientos[0].__dict__.keys())
            for clave in CLAVES_IGNORADAS:
                fieldnames.remove(clave)

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                for clave in CLAVES_IGNORADAS:
                    mov_dict.pop(clave)
                writer.writerow(mov_dict)
           

    def __str__(self):
        """
        Pinta la lista de movimientos por pantall (consola)
        """
        if len(self.movimientos) > 0:
            resultado = ""
            for mov in self.movimientos:
                resultado += f'{mov}\n'
        else:
            resultado = 'La lista de movimientos está vacía'
        return resultado

    
    def __repr__(self):
        conteo = len(self.movimientos)
        return f'Lista de movimientos con {conteo} movimientos'
