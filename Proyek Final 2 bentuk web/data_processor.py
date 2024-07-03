import pandas as pd

def read_csv_data(file_path):
    # Membaca file CSV tanpa baris header, dan menambahkan nama kolom 'waktu', 'power_out', dan 'gain'
    data_df = pd.read_csv(file_path, header=None, names=['waktu', 'power_out', 'gain'])

    # Mengubah kolom 'waktu' menjadi tipe data datetime
    data_df['waktu'] = pd.to_datetime(data_df['waktu'])
    return data_df

def process_data(data_df):
    # Mengembalikan data yang telah dibaca tanpa perubahan
    return data_df