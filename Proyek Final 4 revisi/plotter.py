import plotly.graph_objs as go

def plot_data(data_df):
    # Plot untuk Gain terhadap Waktu
    fig_gain = go.Figure()
    fig_gain.add_trace(go.Scatter(x=data_df['waktu'], y=data_df['gain'], mode='lines', name='Gain', line=dict(color='blue')))
    fig_gain.update_layout(
        title='Grafik Gain terhadap Waktu',
        xaxis_title='Waktu',
        yaxis_title='Gain',
        showlegend=True,
        hovermode='x'
    )
    plot_html_gain = fig_gain.to_html(full_html=False)

    # Plot untuk Power Out terhadap Waktu
    fig_power = go.Figure()
    fig_power.add_trace(go.Scatter(x=data_df['waktu'], y=data_df['power_out'], mode='lines', name='Power Out', line=dict(color='green')))
    fig_power.update_layout(
        title='Grafik Power Out terhadap Waktu',
        xaxis_title='Waktu',
        yaxis_title='Power Out',
        showlegend=True,
        hovermode='x'
    )
    plot_html_power = fig_power.to_html(full_html=False)

    return plot_html_gain, plot_html_power
