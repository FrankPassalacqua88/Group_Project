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


# %%
# Import necessary libraries
import plotly.graph_objs as go
import plotly.offline as pyo
import plotly.subplots as sp
import numpy as np

# Create figure
fig = go.Figure()

selected_year = 2020

# Define function to sort data by GDP and Total_Score
def sort_data_by_selected_year(selected_year):
    df_filtered_pop = df[df['Year'] == selected_year].sort_values(by='Population', ascending=True)
    df_filtered_gdp = df[df['Year'] == selected_year].sort_values(by='GDP', ascending=True)
    df_filtered_score = df[df['Year'] == selected_year].sort_values(by='Total_Medals', ascending=True)
    return df_filtered_gdp, df_filtered_pop, df_filtered_score

# Create two subplots
fig = sp.make_subplots(rows=1, cols=3)

# Add first chart to subplot 1

df_filtered_pop, df_filtered_gdp, df_filtered_score = sort_data_by_selected_year(df['Year'].max())

df_filtered_pop = df[df['Year'] == selected_year].sort_values(by='Population', ascending=True)
fig.add_trace(go.Bar(
    y=df_filtered_pop['Country_Name'],
    x=df_filtered_pop['Population'],
    name='Population',
    marker_color='red',
    orientation='h',
    marker=dict(opacity=0.75)
), row=1, col=1)
# Add title to x-axis of subplot 1
fig.update_xaxes(title_text='Top Population', row=1, col=1)

# Add second chart to subplot 2
df_filtered_gdp = df[df['Year'] == selected_year].sort_values(by='GDP', ascending=True)
fig.add_trace(go.Bar(

  y=df_filtered_gdp['Country_Name'],
    x=df_filtered_gdp['GDP'],
    name='GDP',
    marker_color='green',
    orientation='h',
    marker=dict(opacity=0.75)

), row=1, col=2)
# Add title to x-axis of subplot 2
df_filtered_score = df[df['Year'] == selected_year].sort_values(by='Total_Medals', ascending=True)
fig.update_xaxes(title_text='Top GDP', row=1, col=2)

# Add third chart to subplot 3
fig.add_trace(go.Bar(
    y=df_filtered_score['Country_Name'],
    x=df_filtered_score['Total_Medals'],
    name='Total_Medals',
    marker_color='blue',
    orientation='h',
    marker=dict(opacity=0.75)
), row=1, col=3)
# Add title to x-axis of subplot 3
fig.update_xaxes(title_text='Top Medals for Year', row=1, col=3)

# Update layout
fig.update_layout(title=f'Country Population, GDP, and Medals in {df["Year"].max()}',
                  height=600, width=1000,
                  barmode='group',
                  showlegend=False)

# Create dropdown list of years
years = np.sort(df['Year'].unique())[::-1]
dropdown_buttons = []
for year in years:
    df_filtered_gdp, df_filtered_pop, df_filtered_score = sort_data_by_selected_year(year)
    dropdown_buttons.append(dict(
        label=str(year),
        method="update",
        args=[{
                "x": [df_filtered_pop['Population'],df_filtered_gdp['GDP'], df_filtered_score['Total_Medals']],
                "y": [df_filtered_pop['Country_Name'], df_filtered_gdp['Country_Name'], df_filtered_score['Country_Name']],
                "type": "bar",
                "orientation": "h",
                "marker_color": ['red','green','blue'],
                "name": ['Population', 'GDP', 'Total Medals']
              },
              {
                "title": f"Country Population, GDP, and Medal Score in {year}"
            }]
            ))

# Add dropdown
fig.update_layout(
    updatemenus=[dict(
        buttons=dropdown_buttons,
        direction="down",
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.1,
        yanchor="top"
    )]
)

# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Select Year:", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.show()
pyo.plot(fig, filename='myplot.html', auto_open=True)

# %%
# Create figure
fig = go.Figure()

# Define function to sort data by GDP and Total_Score
def sort_data_by_selected_year(selected_year):
    df_filtered_gdp_cap = df[df['Year'] == selected_year].sort_values(by='GDP_per_capita', ascending=True)
    df_filtered_score_cap = df[df['Year'] == selected_year].sort_values(by='Medal_score_per_capita', ascending=True)
    df_filtered_score_gdp = df[df['Year'] == selected_year].sort_values(by='Medal_score_per_GDP', ascending=True)
    return df_filtered_gdp_cap, df_filtered_score_cap, df_filtered_score_gdp

# Create two subplots
fig = sp.make_subplots(rows=1, cols=3)

# Add first chart to subplot 1

df_filtered_gdp_cap,  df_filtered_score_cap,  df_filtered_score_gdp = sort_data_by_selected_year(df['Year'].max())

df_filtered_gdp_cap = df[df['Year'] == selected_year].sort_values(by='GDP_per_capita', ascending=True)
fig.add_trace(go.Bar(
    y=df_filtered_gdp_cap['Country_Name'],
    x=df_filtered_gdp_cap['GDP_per_capita'],
    name='GDP_per_capita',
    marker_color='red',
    orientation='h',
    marker=dict(opacity=0.75)
), row=1, col=1)
# Add title to x-axis of subplot 1
fig.update_xaxes(title_text='Top GDP_per_capita', row=1, col=1)

# Add second chart to subplot 2
df_filtered_score_cap = df[df['Year'] == selected_year].sort_values(by='Medal_score_per_capita', ascending=True)
fig.add_trace(go.Bar(

  y=df_filtered_score_cap['Country_Name'],
    x=df_filtered_score_cap['Medal_score_per_capita'],
    name='Medal_score_per_capita',
    marker_color='green',
    orientation='h',
    marker=dict(opacity=0.75)

), row=1, col=2)
# Add title to x-axis of subplot 2
df_filtered_score_cap = df[df['Year'] == selected_year].sort_values(by='Medal_score_per_capita', ascending=True)
fig.update_xaxes(title_text='Medal_score_per_capita', row=1, col=2)

# Add third chart to subplot 3
fig.add_trace(go.Bar(
    y=df_filtered_score_gdp['Country_Name'],
    x=df_filtered_score_gdp['Medal_score_per_GDP'],
    name='Medal_score_per_GDP',
    marker_color='blue',
    orientation='h',
    marker=dict(opacity=0.75)
), row=1, col=3)
# Add title to x-axis of subplot 3
fig.update_xaxes(title_text='Medal_score_per_GDP', row=1, col=3)

# Update layout
fig.update_layout(title=f'Country GDP Per Capita Stats {df["Year"].max()}',
                  height=600, width=1000,
                  barmode='group',
                  showlegend=False)

# Create dropdown list of years
years = np.sort(df['Year'].unique())[::-1]
dropdown_buttons = []
for year in years:
    df_filtered_gdp_cap, df_filtered_score_cap, df_filtered_score_gdp = sort_data_by_selected_year(year)
    dropdown_buttons.append(dict(
        label=str(year),
        method="update",
        args=[{
                "x": [df_filtered_gdp_cap['GDP_per_capita'],df_filtered_score_cap['Medal_score_per_capita'], df_filtered_score_gdp['Medal_score_per_GDP']],
                "y": [df_filtered_gdp_cap['Country_Name'], df_filtered_score_cap['Country_Name'], df_filtered_score_gdp['Country_Name']],
                "type": "bar",
                "orientation": "h",
                "marker_color": ['red','green','blue'],
                "name": ['GDP_per_capita', 'Medal_score_per_capita', 'Medal_score_per_GDP'],
            },
              {
                "title": f"Country Population, GDP, and Medal Score in {year}"
            }]
    ))

# Add dropdown
fig.update_layout(
    updatemenus=[dict(
        buttons=dropdown_buttons,
        direction="down",
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.1,
        yanchor="top"
    )]
)

# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Select Year:", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.show()

# %%
fig.add_trace(go.Bar(
    y=df_filtered_gdp_cap['Country_Name'],
    x=df_filtered_gdp_cap['GDP_per_capita'],
    name='GDP_per_capita',
    marker_color='red',
    orientation='h',
    marker=dict(opacity=0.75)
))

# %%
import plotly.express as px

fig = px.colors.qualitative.swatches()
print(px.colors.qualitative.Light24)
print(px.colors.qualitative.D3)
print(px.colors.qualitative.G10)
print(px.colors.qualitative.T10)
print(px.colors.qualitative.Alphabet)
fig.show()

# %%



