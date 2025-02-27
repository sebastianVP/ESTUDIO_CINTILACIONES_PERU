import os
import subprocess

def process_directories(input_directories):
    for input_directory in input_directories:
        print(f"Procesando directorio: {input_directory}")
        try:
            # Cambiar al directorio actual
            os.chdir(input_directory)

            # Ejecutar el comando gzip -d *
            print(f"Descomprimiendo archivos en {input_directory}...")
            subprocess.run(["gzip -d *"], shell=True, check=True)

            print(f"Archivos descomprimidos en {input_directory}")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando en {input_directory}: {e}")
        except Exception as e:
            print(f"Error al procesar el directorio {input_directory}: {e}")



# Ruta del directorio de entrada y archivo de salida
PATH="/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA"
months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]
# Lista de directorios a procesar
input_directories= [os.path.join(PATH,os.path.join(f"2024_{month}_scint_data_ljic","data")) for month in months]
print("Input_directories: ",input_directories)
process_directories(input_directories)