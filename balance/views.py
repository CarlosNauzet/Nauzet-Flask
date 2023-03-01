from flask import render_template

from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados
    """
    return render_template("inicio.html")

@app.route('/nuevo')
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    return "Crea movimiento"

@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento
    """
    return "Actualizar movimiento"

@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return "Eliminar movimiento"
