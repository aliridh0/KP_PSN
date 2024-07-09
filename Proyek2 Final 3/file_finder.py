import os

def find_csv_files(folder_path, physical_port):
    physical_port = str(physical_port)  # Pastikan physical_port adalah string
    files = []
    for file_name in os.listdir(folder_path):
        if file_name.startswith(physical_port) and file_name.endswith('.csv'):
            files.append(os.path.join(folder_path, file_name))
    return files

def save_combined_csv(data_df, output_folder, physical_port):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    combined_file_path = os.path.join(output_folder, f"{physical_port}.csv")
    data_df.to_csv(combined_file_path, index=False)
    return combined_file_path
