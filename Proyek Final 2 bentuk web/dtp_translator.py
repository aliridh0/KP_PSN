import pandas as pd

def load_dtp_subchannel(file_path):
    # Membaca file Excel yang berisi data DTP Subchannel
    return pd.read_excel(file_path)

def translate_port(logical_port, dtp_df):
    # Mencari baris yang sesuai dengan Logical_OutputPort yang diberikan
    row = dtp_df.loc[dtp_df['Logical_OutputPort'] == logical_port]
    
    if not row.empty:
        # Jika baris ditemukan, kembalikan nilai Physical_OutputPort
        return row['Physical_OutputPort'].values[0]
    else:
        # Jika tidak ditemukan, kembalikan None
        return None