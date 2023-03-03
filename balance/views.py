from flask import redirect, render_template, request, url_for

from . import app
from .models import ListaMovimientos, Movimiento


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    
    return render_template("inicio.html", movs = lista.movimientos)

@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV

    1. Recibo una petición GET: pinto el formulario
    2. Recibo una petición POST: 
        - Recojo los datos del formulario
        - Creo un movimiento con los datos que llegan
        - Compruebo que el movimiento no tiene errores (validación)
        - Utilizo la lista de movimientos para agregar el nuevo movimiento ( se guarda en el archivo CS)
        - Redirección a la página home ( la que tiene la tabla de movimientos )
    """
    if request.method == 'GET':
        return render_template("nuevo.html")
    if request.method == 'POST':
        datos = request.form
        movimiento = Movimiento(datos)
        lista = ListaMovimientos()
        lista.leer_desde_archivo()
        lista.agregar(movimiento)
        return redirect(url_for('home'))

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
