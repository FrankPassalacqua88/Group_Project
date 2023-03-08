import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# %%
import pandas as pd
import numpy as np
import plotly.subplots as sp

# %% [markdown]
# ## Import Tables

# %%
df = pd.read_csv('../calculations_per_capita_and_medal_score.csv')
df.tail()

# %%
df = df.drop('Unnamed: 0', axis=1)
df.head()

# %%
# Define all rows with missing data
zero_gdp_pop_rows = df[(df['GDP'] == 0) | (df['Population'] == 0)]
zero_gdp_pop_rows.head()

# %%
# Drop the rows with zero GDP and/or Population
df = df.drop(zero_gdp_pop_rows.index)
df.head()

# %%
df.describe()

# %%
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Filter data by year
selected_year = 2020
df_filtered = df[df['Year'] == selected_year].sort_values(by='GDP', ascending=True)

# Create three subplots with different number of columns
fig = make_subplots(rows=1, cols=3)

# Add first chart to subplot 1
fig.add_trace(go.Bar(
    y=df_filtered['Country_Name'],
    x=df_filtered['GDP'],
    name='GDP',
    marker_color='lightsalmon',
    orientation='h'
), row=1, col=1)
fig.update_xaxes(title_text='Top GDP', row=1, col=1)
# Add second chart to subplot 2
df_filtered = df[df['Year'] == selected_year].sort_values(by='Total_Medals', ascending=True)
fig.add_trace(go.Bar(
    y=df_filtered['Country_Name'],
    x=df_filtered['Total_Medals'],
    name='Total Medals',
    marker_color='indianred',
    orientation='h'
), row=1, col=2)
fig.update_xaxes(title_text='Top Medal Count', row=1, col=2)
# Add second chart to subplot 2
df_filtered = df[df['Year'] == selected_year].sort_values(by='Total_Score', ascending=True)
fig.add_trace(go.Bar(
    y=df_filtered['Country_Name'],
    x=df_filtered['Total_Score'],
    name='Total Score',
    marker_color='red',
    orientation='h'
), row=1, col=3)
fig.update_xaxes(title_text='Top Medal Score', row=1, col=3)
# Update layout to set grid with 2 columns for the second row
fig.update_layout(title=f'Country GDP and Medal Count Vs Medal Score {selected_year}', 
                  height=600, width=1000, 
                  barmode='group',
                  showlegend=False)

fig.show()


import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import requests, base64
from io import BytesIO
import dash_core_components as dcc
import plotly.graph_objs as go
from collections import Counter
# import dash_core_components as dcc    #deprecated
from dash import dcc 
# import dash_html_components as html    #deprecated
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter