import matplotlib.pyplot as plt

def plot_data(data_df):
    # Membuat gambar berukuran 12x10 inci dengan 2 subplot
    plt.figure(figsize=(12, 10))

    # Subplot pertama untuk grafik Gain terhadap Waktu
    plt.subplot(2, 1, 1)
    plt.plot(data_df['waktu'], data_df['gain'], label='Gain', color='blue')
    plt.xlabel('Waktu') # Label sumbu x
    plt.ylabel('Gain') # Label sumbu y
    plt.title('Grafik Hubungan Waktu dengan Gain') # Judul plot
    plt.legend() # Menampilkan legenda
    plt.grid(True) # Menampilkan grid

    # Subplot kedua untuk grafik Power Out terhadap Waktu
    plt.subplot(2, 1, 2)
    plt.plot(data_df['waktu'], data_df['power_out'], label='Power Out', color='green')
    plt.xlabel('Waktu') # Label sumbu x
    plt.ylabel('Power Out') # Label sumbu y
    plt.title('Grafik Hubungan Waktu dengan Power Out') # Judul plot
    plt.legend()    # Menampilkan legenda
    plt.grid(True)  # Menampilkan grid

    plt.tight_layout()   # Mengatur layout agar subplot terlihat rapi
    plt.show()           # Menampilkan plot