import pandas as pd
import os
import sys
import plotly.express as px
import plotly.graph_objects as go
import nbformat
import plotly.io as pio
import ipywidgets as widgets

import streamlit as st

"""
os.chdir('.~recoverytracker')

files = os.listdir()

affinity = pd.read_csv(files[0])
bglass = pd.read_csv(files[1])
covid_deaths = pd.read_csv(files[2])
covid_cases = pd.read_csv(files[3])
geo_id = pd.read_csv(files[4])
google_mobility = pd.read_csv(files[5])
low_inc_earn_all = pd.read_csv(files[6])
low_inc_earn_small = pd.read_csv(files[7])
low_inc_emp_all = pd.read_csv(files[8])
ui_claims = pd.read_csv(files[9])
merchants = pd.read_csv(files[10])

df = pd.concat([affinity, bglass, covid_deaths, covid_cases, google_mobility, low_inc_earn_all, low_inc_earn_small, low_inc_emp_all, ui_claims, merchants])
df = df.merge(geo_id, on='cityid', how='left')
df.dropna(subset=['day', 'month', 'year'], inplace=True)

df.day = df.day.astype(int)
df.month = df.month.astype(int)
df.year = df.year.astype(int)

df['date'] = df.month.astype(str) + "/" + df.day.astype(str) + "/" + df.year.astype(str)
df.date = pd.to_datetime(df.date)
df.gps_away_from_home = df.gps_away_from_home * 100
df.spend_all = df.spend_all * 100

df.to_csv('data.csv', index=False)

# Create city subsets
# Check cityid names for subsetting
#df[['cityname', 'cityid']].drop_duplicates()
"""
df = read_csv('data.csv')

st.title('Covid Tracker')

def make_graph(i, j):
    # Create figure
    plot = go.FigureWidget()

    plot.add_scatter(x=df[df.cityname == i].date, y=df[df.cityname == i][j])
    plot.update_traces(textposition='top center', showlegend=False)
    plot.update_layout(title = str(j + ' in ' + i), title_x=0.5, template="plotly_dark")

    plot.show()

df.cityname.unique()

st.subheader('Select City')
city = st.selectbox('Choose One', geo_id.cityname.unique())

st.subheader('Select Variable to Visualize')
var = st.selectbox('Choose One', df.columns)

if st.button('Generate Graph!'):
    st.dataframe(df[df.cityname == city])
    make_graph(city, var)
