from flask import Flask, render_template, request, redirect, url_for, flash
from dtp_translator import load_dtp_subchannel, translate_port
from file_finder import find_csv_file
from data_processor import read_csv_data, process_data
from plotter import plot_data
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load DTP Subchannel data
dtp_df = load_dtp_subchannel('DTP subchannel.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logical_port_number = request.form['logical_port']
        subchannel = request.form['subchannel']
        logical_port = f"DTPO-{logical_port_number}"

        # Translate Logical_OutputPort to Physical_OutputPort
        physical_port = translate_port(logical_port, dtp_df)
        if physical_port is None:
            flash(f"Physical_OutputPort untuk {logical_port} tidak ditemukan.", 'error')
            return redirect(url_for('index'))

        # Find the corresponding CSV file
        file_path = find_csv_file('TEMP_OUTPUT_PWR240624', physical_port, subchannel)
        if file_path is None:
            flash(f"File CSV untuk {physical_port}_{subchannel} tidak ditemukan.", 'error')
            return redirect(url_for('index'))

        # Read and process data from CSV file
        data_df = read_csv_data(file_path)
        processed_data_df = process_data(data_df)

        # Plot data using Plotly
        plot_html_gain, plot_html_power = plot_data(processed_data_df)

        flash(f"Data berhasil diproses untuk {logical_port} SubChannel-{subchannel} dan plot telah ditampilkan.", 'success')
        return render_template('index.html', plot_html_gain=plot_html_gain, plot_html_power=plot_html_power)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
