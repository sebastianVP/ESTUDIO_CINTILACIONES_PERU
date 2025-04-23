## USO DE LA LIBRERIA CKAN PARA EXTRAER BLOQUES DE DATOS##
# pip install -e git+http://intranet.igp.gob.pe:8082/DATABASES/ckanext-jro/api-cliente#egg=jrodb
# NEW LINK DE LISN - https://lisn.igp.gob.pe/database 
# PROBAR EL LINK Y VERIFICAR

# USAR SERVIDOR PEDIR A GOMERO SI ESTOY DESDE EL ROJ . 

from src.jrodb.jrodb import Api
import os
#print("Test de la libreria")
#print(Api.download.__doc__)

from jrodb import Api
# DESCARGAMOS EL CONJUNTO DE DATOS

# Lista de los meses en minúsculas
years  = ["2023","2024","2025"]
#years  = ["2023"]
months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

print(months)

# JICAMARCA jic
# HUANCAYO hyo

# ESTACION S4 ENCONTRADAS DESPUES DE REVISION S4 EN LISN
# CUZCO,JAEN,JICAMARCA,PIURA,HUANCAYO,SAN_BARTOLOME,PUCP,PUCALLPA
#station="puc"    #"tac" "cuz" #"puc" #"piu"# "hyo" # "jic"
#DIR= "PUCALLPA"  #"TACNA" "CUZCO" #"PUCALLPA" #"PIURA" #"HUANCAYO" "JICAMARCA"

stations = ["cuz","jae","jic","piu","hyo","sbr","ucp","puc"]
DIRS     = ["CUZCO","JAEN","JICAMARCA","PIURA","HUANCAYO","SAN_BARTOLOME","PUCP","PUCALLPA"]
stations = ["jic"]
DIRS     = ["JICAMARCA"]

#----------------------------------------------------------------------------------------
# NO ENCUENTRO PARAMETRO S4, TACNA, PUERTO MALDONADO
# --------------------------------------DESCARGA DATOS ESTACION JICAMARCA----------------
for station,DIR in zip(stations, DIRS):
  for year in years:
      for month in months:
        print("--------------------------------------------------------")
        print(f"Descargando el mes {month}...| STATION: {station} | DIR : {DIR}")
        print("--------------------------------------------------------")
        # Define la ruta donde se guardarán los datos
        path = f"/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA/DATA_S4/{DIR}"
        # Crea el directorio si no existe
        os.makedirs(path, exist_ok=True)
        # Accede a la API y descarga los datos
        with Api('https://lisn.igp.gob.pe/database') as access:
        #with Api('https://www.igp.gob.pe/observatorios/radio-observatorio-jicamarca/database-cielo') a access:
           id = f'{year}_{month}_scint_data_l{station}'
           print(access.download(id =id ,path=f"/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA/DATA_S4/{DIR}"))

# LUEGO DESCOMPRIMIMOS CON EL COMANDO
# gzip -d *
