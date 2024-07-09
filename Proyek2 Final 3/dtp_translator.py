import pandas as pd

def load_dtp_subchannel(file_path):
    return pd.read_excel(file_path)

def translate_port(logical_port, dtp_df):
    row = dtp_df.loc[dtp_df['Logical_OutputPort'] == logical_port]
    if not row.empty:
        return str(row['Physical_OutputPort'].values[0])  # Pastikan mengembalikan string
    else:
        return None
