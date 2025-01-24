## USO DE LA LIBRERIA CKAN PARA EXTRAER BLOQUES DE DATOS##
# pip install -e git+http://intranet.igp.gob.pe:8082/DATABASES/ckanext-jro/api-cliente#egg=jrodb

from src.jrodb.jrodb import Api
#print("Test de la libreria")
#print(Api.download.__doc__)

from jrodb import Api
# DESCARGAMOS EL CONJUNTO DE DATOS

with Api('https://www.igp.gob.pe/observatorios/radio-observatorio-jicamarca/database-cielo') as access:
  print(access.download(id ='2024_december_scint_data_ljic',path="/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/Diciembre"))

# LUEGO DESCOMPRIMIMOS CON EL COMANDO
# gzip -d *
