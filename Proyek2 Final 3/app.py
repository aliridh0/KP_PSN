from flask import Flask, render_template, request, redirect, url_for, flash
from dtp_translator import load_dtp_subchannel, translate_port
from file_finder import find_csv_files, save_combined_csv
from data_processor import read_csv_data, process_data
from plotter import plot_data
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load DTP Subchannel data
dtp_df = load_dtp_subchannel('DTP subchannel.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logical_port_number = request.form['logical_port']
        logical_port = f"DTPO-{logical_port_number}"

        # Translate Logical_OutputPort to Physical_OutputPort
        physical_port = translate_port(logical_port, dtp_df)
        if physical_port is None:
            flash(f"Physical_OutputPort untuk {logical_port} tidak ditemukan.", 'error')
            return redirect(url_for('index'))

        # Find all corresponding CSV files for the Physical_OutputPort
        file_paths = find_csv_files('TEMP_OUTPUT_PWR', physical_port)
        if not file_paths:
            flash(f"Tidak ada file CSV untuk {physical_port} ditemukan.", 'error')
            return redirect(url_for('index'))

        # Read and process data from all CSV files
        combined_data_df = pd.DataFrame()
        for file_path in file_paths:
            data_df = read_csv_data(file_path)
            combined_data_df = pd.concat([combined_data_df, data_df], ignore_index=True)

        processed_data_df = process_data(combined_data_df)

        # Save processed data to new CSV file
        output_folder = 'Combined_Output'
        combined_file_path = save_combined_csv(processed_data_df, output_folder, physical_port)

        # Plot data using Plotly
        plot_html_gain, plot_html_power = plot_data(processed_data_df)

        flash(f"Data berhasil diproses untuk {logical_port} dan plot telah ditampilkan.", 'success')
        return render_template('index.html', plot_html_gain=plot_html_gain, plot_html_power=plot_html_power)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
