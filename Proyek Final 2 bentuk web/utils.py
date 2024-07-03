def get_user_input():
    # Meminta pengguna untuk memasukkan nomor Logical_OutputPort
    logical_port_number = input("Masukkan nomor Logical_OutputPort (misal: 28 untuk DTPO-28): ")

    # Membuat string Logical_OutputPort berdasarkan input pengguna
    logical_port = f"DTPO-{logical_port_number}"

    # Meminta pengguna untuk memasukkan Subchannel
    subchannel = input("Masukkan Subchannel: ")

    # Mengembalikan nilai logical_port dan subchannel sebagai tuple
    return logical_port, subchannel