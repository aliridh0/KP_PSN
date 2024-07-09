import pandas as pd
import math

def read_csv_data(file_path):
    # Membaca file CSV tanpa baris header, dan menambahkan nama kolom 'waktu', 'power_out', dan 'gain'
    data_df = pd.read_csv(file_path, header=None, names=['waktu', 'gain', 'power_out'])

    # Mengubah kolom 'waktu' menjadi tipe data datetime
    data_df['waktu'] = pd.to_datetime(data_df['waktu'])
    return data_df

def process_data(data_df):
    # Menghitung gain dan power output dalam dBW
    data_df['gain_dBW'] = data_df['gain']
    data_df['power_out_dBW'] = data_df['power_out'] - 30

    # Menghitung gain dan power output numerik
    data_df['gain_numerik'] = (10 ** ((data_df['gain_dBW']) / 10))/1000
    data_df['power_out_numerik'] = 1000 * (10 ** (data_df['power_out_dBW'] / 10))



    # Mengelompokkan data berdasarkan rentang waktu 7 menit dan menghitung jumlah
    data_df.set_index('waktu', inplace=True)
    data_df_resampled = data_df.resample('7T').sum()

    # Menambahkan kolom waktu untuk hasil yang diresample
    data_df_resampled['waktu'] = data_df_resampled.index

    return data_df_resampled.reset_index(drop=True)
