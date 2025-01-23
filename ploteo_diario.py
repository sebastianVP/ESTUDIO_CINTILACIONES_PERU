import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import matplotlib
matplotlib.use('Agg')  # Usar backend sin interfaz gráfica0

# Cargar los datos del archivo CSV
input_csv_path = 'output_satellites_data.csv'
data = pd.read_csv(input_csv_path)

# Convertir la columna de tiempo a formato datetime
data['Tiempo'] = pd.to_datetime(data['Tiempo'])

# Obtener la lista de satélites únicos, ordenados de menor a mayor
satellites = sorted(data['ID Satélite'].unique())

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
        sat_data = data[data['ID Satélite'] == satellite_id]

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
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.tick_params(axis='x', rotation=45, labelsize=8)
        ax.grid(visible=True, linestyle='--', alpha=0.5)

    # Eliminar subplots vacíos si hay menos de 40 satélites
    for empty_ax in axes[end - start:]:
        empty_ax.axis('off')

    # Guardar la figura actual
    output_plot_path = f'satellites_group_{fig_index + 1}_plot.png'
    plt.savefig(output_plot_path, dpi=300)
    plt.close()

print("Gráficos en subplots generados y guardados.")

