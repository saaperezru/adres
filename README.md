# Requerimientos
Idealmente se espera que tenga Nix y DirENV instalados en la máquina para aprovechar las especificaciones en los archivos .envrc y shell.nix
De lo contrario se asume que los siguientes paquetes están instalados:
 - Python 3.12
 - Poetry 1.8.3
 - Sqlite3
 - Poppler

# Instalación
## Con Nix y DirENV
Ejecute el comando

```bash
dir env allow .
```
Luego
```bash
poetry install
```
## Sin Nix ni DirENV
Ejecute
```bash
poetry install
```
# Uso
## Validador CSV
```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

## Extractor PDF
Software para extraer el CUFE de archivos PDF a una BD SQLite
# Bash
Agrupe todos los PDF que quiere analizar en una sola carpeta `FOLDER`
Y luego ejecute el comando
```bash
chmod +x extract.sh
./extract.sh <FOLDER> <DBFILE>
```
Donde `<DBFILE>` debe ser el nombre a usar para la base de datos SQLite que contenga la información extraída.
Al terminar el comando verá una base de datos con las siguientes columnas:
 - file_name
 - cufe
 - pages
 - size_bytes
