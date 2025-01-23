from datetime import datetime,timedelta
import os
def parse_septentrio_data(sep_file_path):
    sep_satellites_data = {}

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

                # Almacenar los datos por satélite
                if id_satellite not in sep_satellites_data:
                    sep_satellites_data[id_satellite] = {'tiempo': [], 's4': [], 'elevacion': []}

                sep_satellites_data[id_satellite]['tiempo'].append(time)
                sep_satellites_data[id_satellite]['s4'].append(s4)
                sep_satellites_data[id_satellite]['elevacion'].append(elevation)

                index += 4

    return sep_satellites_data

sep_folder_path = "/home/soporte/Documents/PAPER_CINTILACION"
sep_file = "ljic_241231.s4"
sep_file_path = os.path.join(sep_folder_path, sep_file)
septentrio_sat_data = parse_septentrio_data(sep_file_path)
print(septentrio_sat_data)