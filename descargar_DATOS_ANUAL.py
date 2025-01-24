## USO DE LA LIBRERIA CKAN PARA EXTRAER BLOQUES DE DATOS##
# pip install -e git+http://intranet.igp.gob.pe:8082/DATABASES/ckanext-jro/api-cliente#egg=jrodb

from src.jrodb.jrodb import Api
#print("Test de la libreria")
#print(Api.download.__doc__)

from jrodb import Api
# DESCARGAMOS EL CONJUNTO DE DATOS

# Lista de los meses en minúsculas
years= ["2023"]
months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

print(months)
for year in years:
    for month in months:
        print(f"Descargando el mes {month}...")
        with Api('https://www.igp.gob.pe/observatorios/radio-observatorio-jicamarca/database-cielo') as access:       
            id = f'{year}_{month}_scint_data_ljic'
            print(access.download(id =id ,path="/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA"))

# LUEGO DESCOMPRIMIMOS CON EL COMANDO
# gzip -d *
