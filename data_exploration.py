# coding=utf-8
import os
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
from preprocess import preprocess

path = './2004-2019.tsv'
df = pd.read_csv(path, sep='\t', parse_dates=True)
df = preprocess(df)

def count_observation_per_region(df):

    st.subheader('Context')
    # Translate region name to english and replace
    st.write(
        'The macro-region column represents the subdivisions there are in Brazil. There are 5 Region.')

    ds = {"col1": ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"],
            "col2": ["South", "Southeast", "Mideast", "Northeast", "North"]}
    header = pd.DataFrame(ds)
    # header_df = pd.dataframe(data=ds)
    st.table(header)

    sample = st.sidebar.selectbox(
        'Enter sample size for Region', (500, 1000, 1500, 2000)
    )

    c = alt.Chart(df.head(sample), title='Number of Observations by Region').mark_bar().encode(
        x='Macroregion',
        y='count()'
    ).properties(
        width=600,
        height=500
    )

    st.altair_chart(c)

    st.dataframe(df['Macroregion'].head(
        sample).value_counts(normalize=True))


def number_of_observation_by_state(df):
    sample_2 = st.sidebar.selectbox(
        'Enter sample size for State', (500, 1000, 1500, 2000)
    )

    d = alt.Chart(df.head(sample_2), title="Number of Observations by State").mark_bar().encode(
        x='State',
        y='count()',
    ).properties(
        width=500,
        height=400
    )

    st.write(d)
    st.dataframe(df['State'].head(sample_2).value_counts(normalize=True))


def number_of_gas_stations_per_state(df):
    sample_3 = st.sidebar.selectbox(
        'Enter sample size for number of gas stations per state', (
            500, 1000, 1500, 2000)
    )
    e = alt.Chart(df.head(sample_3), title="Number of Gas Stations per State").mark_bar().encode(
        x='State',
        y='No_of_Gas_Stations_Analyzed'
    ).properties(
        width=500,
        height=400
    )

    st.write(e)
    st.dataframe(
        df['No_of_Gas_Stations_Analyzed'].head(sample_3).value_counts(normalize=True))