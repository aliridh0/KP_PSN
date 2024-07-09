import plotly.graph_objs as go

def plot_data(data_df):
    # Plot untuk Sum Gain Numerik terhadap Waktu
    fig_gain = go.Figure()
    fig_gain.add_trace(go.Scatter(x=data_df['waktu'], y=data_df['gain_numerik'], mode='lines', name='Sum Gain Numerik', line=dict(color='blue')))
    fig_gain.update_layout(
        title='Sum Gain Numerik terhadap Waktu dalam Rentang 7 Menit',
        xaxis_title='Waktu',
        yaxis_title='Sum Gain Numerik',
        showlegend=True,
        hovermode='x'
    )
    plot_html_gain = fig_gain.to_html(full_html=False)

    # Plot untuk Sum Power Output Numerik terhadap Waktu
    fig_power = go.Figure()
    fig_power.add_trace(go.Scatter(x=data_df['waktu'], y=data_df['power_out_numerik'], mode='lines', name='Sum Power Output Numerik', line=dict(color='green')))
    fig_power.update_layout(
        title='Sum Power Output Numerik terhadap Waktu dalam Rentang 7 Menit',
        xaxis_title='Waktu',
        yaxis_title='Sum Power Output Numerik',
        showlegend=True,
        hovermode='x'
    )
    plot_html_power = fig_power.to_html(full_html=False)


    return plot_html_gain, plot_html_power
