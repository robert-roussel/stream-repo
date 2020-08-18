import pandas as pd
import os
import sys
import plotly.express as px
import plotly.graph_objects as go
import nbformat
import plotly.io as pio
import ipywidgets as widgets

import streamlit as st

df = pd.read_csv('https://github.com/robert-roussel/stream-repo/blob/master/data.csv?raw=true', low_memory=False)

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
