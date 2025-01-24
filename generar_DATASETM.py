from datetime import datetime, timedelta
import os
import csv

def parse_septentrio_data(sep_file_path):
    sep_satellites_data = []

    with open(sep_file_path, 'r') as sep_file:
        for line in sep_file:
            parts = line.strip().split()

            # Extraer datos generales
            year = int(parts[0]) + 2000  # Año en formato completo
            day_of_year = int(parts[1])
            seconds_from_midnight = int(parts[2])
            num_satellites = int(parts[3])

            # Convertir el día del año y segundos en una fecha y hora
            date_base = datetime(year, 1, 1)
            time = date_base + timedelta(days=day_of_year - 1, seconds=seconds_from_midnight)

            # Procesar los datos de los satélites
            index = 4
            for _ in range(num_satellites):
                id_satellite = int(parts[index])
                s4 = float(parts[index + 1])
                azimut = float(parts[index + 2])
                elevation = float(parts[index + 3])

                # Almacenar los datos como una lista de diccionarios
                sep_satellites_data.append({
                    'id_satellite': id_satellite,
                    'time': time,
                    's4': s4,
                    'elevation': elevation
                })

                index += 4

    return sep_satellites_data

def save_to_csv(all_data, output_csv_path):
    # Ordenar los datos por 'id_satellite' y luego por 'time'
    all_data.sort(key=lambda x: (x['id_satellite'], x['time']))

    # Guardar en un archivo CSV
    with open(output_csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID Satélite', 'Tiempo', 'S4', 'Elevación'])

        for entry in all_data:
            csvwriter.writerow([entry['id_satellite'], entry['time'], entry['s4'], entry['elevation']])

def process_directories(input_directories, output_csv_path):
    all_data = []

    # Recorrer cada directorio en la lista
    for input_directory in input_directories:
        print(f"Procesando directorio: {input_directory}")
        for file_name in os.listdir(input_directory):
            if file_name.endswith('.s4'):  # Filtrar por extensión .s4
                file_path = os.path.join(input_directory, file_name)

                if os.path.isfile(file_path):  # Verificar que sea un archivo
                    print(f"Procesando archivo: {file_name}")
                    file_data = parse_septentrio_data(file_path)
                    all_data.extend(file_data)

    # Guardar todos los datos combinados en un solo archivo CSV
    save_to_csv(all_data, output_csv_path)

# Ruta del directorio de entrada y archivo de salida
PATH="/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/DATA"
YEAR="2024"
# Lista de rutas de directorios de entrada

directories= os.listdir(PATH)
months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]
input_directories= [os.path.join(PATH,os.path.join(f"2024_{month}_scint_data_ljic","data")) for month in months]
print("Input_directories: ",input_directories)

output_csv_path = f"{YEAR}_output_combined_satellites_data.csv"

process_directories(input_directories, output_csv_path)

#print(f"Datos combinados guardados en {output_csv_path}")