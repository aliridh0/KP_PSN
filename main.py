import csv
import os
import shutil
from datetime import datetime

# Fungsi untuk menambahkan baris ke file CSV
def ajouter_variables(fichier_csv, nouvelle_ligne_csv):
    with open(fichier_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(nouvelle_ligne_csv)

# Fungsi untuk mendapatkan path folder dari path file
def get_folder_path(file_path):
    return os.path.dirname(file_path)

# Fungsi untuk memproses file CSV
def process_csv_file(csv_file_path):
    folder_path = get_folder_path(csv_file_path)
    output_folder = os.path.join(folder_path, 'TEMP_OUTPUT_PWR')

    # Buat folder temporary jika belum ada
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = row['Date']

            # Proses setiap output port dan ID
            for i in range(1, 10):
                out_port_key = f'DTP_CH_OUTPUT_PORT{i}'
                id_key = f'DTP_CH_ID_OUT_PORT{i}'
                gain_key = f'DTP_CH_MEAS_GAIN_{i}'
                power_key = f'DTP_CH_POWER_16B{i}'

                out_port_value = row[out_port_key]
                id_value = row[id_key]
                gain_value = row[gain_key]
                power_value = row[power_key]

                if out_port_value and id_value and gain_value and power_value:
                    # Buat nama file csv
                    csv_filename = f"{out_port_value}_{id_value}.csv"
                    csv_path = os.path.join(output_folder, csv_filename)

                    # Tulis data ke file CSV
                    with open(csv_path, 'a', newline='') as output_csv:
                        csv_writer = csv.writer(output_csv)
                        csv_writer.writerow([date, gain_value, power_value])

    print("Data processing... DONE")

# Jalankan fungsi process_csv_file dengan path file CSV yang benar
csv_file_path = r"D:\INTERN\KP\cleansing\DTP_PORT 04072024.csv" #Sesuaikan dengan directory dari file yang dimiliki dan ubah dulu xml ke excel
process_csv_file(csv_file_path)
