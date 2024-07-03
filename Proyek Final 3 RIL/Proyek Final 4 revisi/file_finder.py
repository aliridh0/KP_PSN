import os

def find_csv_file(folder_path, physical_port, subchannel):
    # Membuat nama file berdasarkan physical_port dan subchannel
    file_name = f"{physical_port}_{subchannel}.csv"

    # Menggabungkan folder_path dengan nama file untuk mencari path lengkap file CSV
    file_path = os.path.join(folder_path, file_name)

    # Memeriksa apakah file CSV ada di lokasi yang ditentukan
    if os.path.exists(file_path):
        return file_path # Mengembalikan path file jika ditemukan
    else:
        return None  # Mengembalikan None jika file tidak ditemukan