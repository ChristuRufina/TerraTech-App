import streamlit as st 
import pandas as pd
import plotly.express as px

# Load data
excel_file = 'crop.xlsx'  
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Streamlit UI
st.set_page_config(page_title='Data Dashboard', layout='wide')
st.header('Data Dashboard 2024 - Proguys')
st.subheader('The data dashboard of crop production')

# Get unique pin codes
unique_pin_codes = df['PIN CODE'].unique()

# Filter by Pin Code
pin_code_selection = st.selectbox('Select Pin Code:', unique_pin_codes)

# Filter data by selected Pin Code
filtered_df = df[df['PIN CODE'] == pin_code_selection]

# Define color sequence
color_sequence = px.colors.qualitative.Plotly

# Plot bar chart for Crop Production by Crop ID
bar_chart = px.bar(filtered_df, 
                   x='CROP ID', 
                   y='CROP PRODUCTION',
                   text='CROP PRODUCTION',
                   color='CROP NAME',
                   template='plotly_white',
                   title='Crop Production by Crop ID',  # Add title
                   labels={'CROP PRODUCTION': 'Crop Production', 'CROP ID': 'Crop ID'},  # Update axis labels
                   width=800,  # Adjust chart width
                   height=500,  # Adjust chart height
                   hover_name='CROP NAME',  # Add hover information
                   hover_data={'CROP ID': False},  # Specify hover data
                   color_discrete_sequence=color_sequence  # Use the same color sequence
                  )

bar_chart.update_layout(
    xaxis=dict(tickfont=dict(size=12)),  # Update x-axis tick font size
    yaxis=dict(tickfont=dict(size=12)),  # Update y-axis tick font size
    font=dict(size=12, color='black'),  # Change global font size and color
    plot_bgcolor='rgba(0,0,0,0)',  # Make plot background transparent
    paper_bgcolor='rgba(0,0,0,0)',  # Make paper background transparent
    showlegend=True,  # Show legend
    legend=dict(title='Crop Name', font=dict(size=12)),  # Update legend font size
)

# Remove gridlines
bar_chart.update_xaxes(showgrid=False)
bar_chart.update_yaxes(showgrid=False)

# Update hover label background color and font size
bar_chart.update_traces(hoverlabel=dict(bgcolor='white', font_size=12))

# Adjust bar width
bar_chart.update_traces(marker=dict(line=dict(width=1, color='gray')))

# Display the bar chart
st.plotly_chart(bar_chart, use_container_width=True)

# Plot pie chart for Crop Production by Crop Name
pie_chart = px.pie(filtered_df, 
                   names='CROP NAME', 
                   values='CROP PRODUCTION',
                   title='Crop Production Distribution by Crop Name',
                   width=800,  # Adjust chart width
                   height=500,  # Adjust chart height
                   color_discrete_sequence=color_sequence  # Use the same color sequence
                  )

# Display the pie chart
st.plotly_chart(pie_chart, use_container_width=True)
