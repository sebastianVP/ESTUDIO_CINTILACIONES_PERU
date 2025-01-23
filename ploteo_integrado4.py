import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import matplotlib
matplotlib.use('Agg')  # Usar backend sin interfaz gráfica


# Cargar los datos del archivo CSV
input_csv_path = 'output_satellites_data.csv'
data = pd.read_csv(input_csv_path)

# Convertir la columna de tiempo a formato datetime
data['Tiempo'] = pd.to_datetime(data['Tiempo'])

# Generar un rango de tiempo completo de 24 horas (intervalos de 1 minuto)
start_time = data['Tiempo'].min().replace(hour=0, minute=0, second=0)
end_time = start_time + pd.Timedelta(days=1)
full_time_range = pd.date_range(start=start_time, end=end_time, freq='1T')

# Completar datos faltantes con NaN para cada satélite
satellites = sorted(data['ID Satélite'].unique())
filled_data = []

for satellite_id in satellites:
    sat_data = data[data['ID Satélite'] == satellite_id]
    sat_data = sat_data.set_index('Tiempo').reindex(full_time_range).reset_index()
    sat_data['ID Satélite'] = satellite_id
    filled_data.append(sat_data)

data_filled = pd.concat(filled_data)
data_filled.rename(columns={'index': 'Tiempo'}, inplace=True)

# Parámetros para subplots
satellites_per_figure = 40
num_figures = math.ceil(len(satellites) / satellites_per_figure)

# Crear gráficos por grupos de 40 satélites
for fig_index in range(num_figures):
    fig, axes = plt.subplots(nrows=8, ncols=5, figsize=(20, 15), constrained_layout=True)
    axes = axes.flatten()

    # Iterar sobre los satélites del grupo actual
    start = fig_index * satellites_per_figure
    end = min(start + satellites_per_figure, len(satellites))
    for idx, satellite_id in enumerate(satellites[start:end]):
        ax = axes[idx]

        # Filtrar los datos del satélite actual
        sat_data = data_filled[data_filled['ID Satélite'] == satellite_id]

        # Gráfico del índice S4 en el eje izquierdo
        ax.plot(sat_data['Tiempo'], sat_data['S4'], label='Índice S4', color='tab:blue')
        ax.set_ylabel('Índice S4', color='tab:blue', fontsize=8)
        ax.tick_params(axis='y', labelcolor='tab:blue', labelsize=8)

        # Gráfico de elevación en el eje derecho
        ax_elevation = ax.twinx()
        ax_elevation.plot(sat_data['Tiempo'], sat_data['Elevación'], label='Elevación', color='tab:orange')
        ax_elevation.set_ylabel('Elevación', color='tab:orange', fontsize=8)
        ax_elevation.tick_params(axis='y', labelcolor='tab:orange', labelsize=8)

        # Configuración del eje X
        ax.set_title(f'Satélite {satellite_id}', fontsize=10)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        ax.tick_params(axis='x', rotation=45, labelsize=7)
        ax.set_xlim([start_time, end_time])  # Asegurar que el eje X vaya de 00:00 a 24:00
        ax.grid(visible=True, linestyle='--', alpha=0.5)

    # Eliminar subplots vacíos si hay menos de 40 satélites
    for empty_ax in axes[end - start:]:
        empty_ax.axis('off')

    # Guardar la figura actual
    output_plot_path = f'/home/soporte/Documents/ESTUDIO_CINTILACIONES_PERU/satellites_group_{fig_index + 1}_plot.png'
    plt.savefig(output_plot_path, dpi=300)
    plt.close()

print("Gráficos en subplots generados y guardados.")
