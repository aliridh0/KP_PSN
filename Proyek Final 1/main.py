from dtp_translator import load_dtp_subchannel, translate_port
from file_finder import find_csv_file
from data_processor import read_csv_data, process_data
from plotter import plot_data
from utils import get_user_input

def main():
    # Memuat data DTP Subchannel dari file Excel
    dtp_df = load_dtp_subchannel('DTP subchannel.xlsx')
    
    while True:
        # Meminta input dari pengguna
        logical_port, subchannel = get_user_input()
        
        # Menerjemahkan Logical_OutputPort menjadi Physical_OutputPort
        physical_port = translate_port(logical_port, dtp_df)
        if physical_port is None:
            print(f"Physical_OutputPort untuk {logical_port} tidak ditemukan.")
            continue
        
        # Mencari file CSV yang sesuai
        file_path = find_csv_file('TEMP_OUTPUT_PWR240624', physical_port, subchannel)
        if file_path is None:
            print(f"File CSV untuk {physical_port}_{subchannel} tidak ditemukan.")
            continue
        
        # Membaca dan memproses data dari file CSV
        data_df = read_csv_data(file_path)
        processed_data_df = process_data(data_df)
        # processed_data1_df = process_data1(data_df) jika mau ditambah proses lain
        
        # Memplot data
        plot_data(processed_data_df)
        # plot_data1(processed_data1_df) jika mau ditambah proses lain
        break

if __name__ == "__main__":
    main()
