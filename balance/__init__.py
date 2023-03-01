import os
from flask import Flask

RUTA_FICHERO = os.path.join("balance", "data", "movimientos.csv")

app = Flask(__name__)


