import matplotlib.pyplot as plt

def plot_data(data_df):
    # Membuat gambar berukuran 12x6 inci dengan 2 subplot
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # Subplot pertama untuk grafik Gain terhadap Waktu
    ax1.plot(data_df['waktu'], data_df['gain'], label='Gain', color='blue')
    ax1.set_xlabel('Waktu')    # Label sumbu x
    ax1.set_ylabel('Gain')     # Label sumbu y
    ax1.set_title('Grafik Hubungan Waktu dengan Gain')   # Judul plot
    ax1.legend()               # Menampilkan legenda
    ax1.grid(True)             # Menampilkan grid

    # Subplot kedua untuk grafik Power Out terhadap Waktu
    ax2.plot(data_df['waktu'], data_df['power_out'], label='Power Out', color='green')
    ax2.set_xlabel('Waktu')    # Label sumbu x
    ax2.set_ylabel('Power Out') # Label sumbu y
    ax2.set_title('Grafik Hubungan Waktu dengan Power Out') # Judul plot
    ax2.legend()               # Menampilkan legenda
    ax2.grid(True)             # Menampilkan grid

    fig.tight_layout()         # Mengatur layout agar subplot terlihat rapi
    plt.show()                 # Menampilkan plot

# Contoh penggunaan fungsi plot_data dengan DataFrame data_df
# Anda dapat menyesuaikan ini dengan memasukkan DataFrame sesuai dengan data yang Anda miliki
# plot_data(data_df)
