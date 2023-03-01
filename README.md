# Nauzet-Flask

Presentación de Flask para desarollo web

## Cómo lanzar el programa en desarrollo

1. Crear un entorno virtual

   ```
   # Windows
   python -m venv env

   # Mac / Linux
   python3 -m venv env
   ```

2. Activar el entorno virtual
   ```
   # Windows
   env\Scripts\activate
   ```
3. Instalar las dependencias
   ```
   pip install -r requirements.txt
   ```
4. Hacer una copia del archivo `.env_template` como `.env`

   ```
    #Windows
    copy .env_template .env

    # Mac / Linux
    cp .env_template .env
   ```

5. Editar el archivo `.env`y cambiar (o no) el valor de ` DEBUG``( `True`/`False`)
