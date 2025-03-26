## USO DE LA LIBRERIA CKAN PARA EXTRAER BLOQUES DE DATOS##
# pip install -e git+http://intranet.igp.gob.pe:8082/DATABASES/ckanext-jro/api-cliente#egg=jrodb
# NEW LINK DE LISN - https://lisn.igp.gob.pe/database 
# PROBAR EL LINK Y VERIFICAR

# USAR SERVIDOR PEDIR A GOMERO SI ESTOY DESDE EL ROJ . 

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
# --------------------------------------DESCARGA DATOS ESTACION JICAMARCA----------------------------------------------------
for year in years:
    for month in months:
        print("--------------------------------------------------------")
        print(f"Descargando el mes {month}...")
        print("--------------------------------------------------------")
        with Api('https://lisn.igp.gob.pe/database') as access:
        #with Api('https://www.igp.gob.pe/observatorios/radio-observatorio-jicamarca/database-cielo') a access:
            id = f'{year}_{month}_scint_data_ljic'
            print(access.download(id =id ,path="/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA/DATA_S4/JICAMARCA"))

# LUEGO DESCOMPRIMIMOS CON EL COMANDO
# gzip -d *
