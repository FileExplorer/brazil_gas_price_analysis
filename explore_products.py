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

def mean_price_of_diesel_over_time_by_state(df):

    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                              fields=['State'], nearest=True)

    h = alt.Chart(df_product_diesel, title='Mean Price of Diesel Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = h.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = h.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_diesel_over_time_by_region(df):

    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    i = alt.Chart(df_product_diesel, title='Mean Price of Diesel Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = i.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = i.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_diesel_s10_over_time_by_state(df):

    df_product_diesels10 = df[df.Product ==
                                'DIESEL S10'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['State'], nearest=True)

    j = alt.Chart(df_product_diesels10, title='Mean Price of Diesel S10 Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = j.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = j.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_diesel_s10_over_time_by_region(df):

    df_product_diesels10 = df[df.Product ==
                                'DIESEL S10'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                              fields=['Macroregion'], nearest=True)

    k = alt.Chart(df_product_diesels10, title='Mean Price of Diesel S10 Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = k.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = k.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_hydrous_ethanol_over_time_by_state(df):

    df_product_hydrousEthanol = df[df.Product ==
                                    'HYDROUS ETHANOL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['State'], nearest=True)

    k = alt.Chart(df_product_hydrousEthanol, title='Mean Price of Hydrous Ethanol Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = k.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = k.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_hydrous_ethanol_over_time_by_region(df):

    df_product_hydrousEthanol = df[df.Product ==
                                    'HYDROUS ETHANOL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    l = alt.Chart(df_product_hydrousEthanol, title='Mean Price of Hydrous Ethanol Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = l.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = l.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_natural_gas_over_time_by_state(df):

    df_product_naturalGas = df[df.Product == 'NATURAL GAS'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    m = alt.Chart(df_product_naturalGas, title='Mean Price of Natural Gas Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = m.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = m.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_natural_gas_over_time_by_region(df):

    df_product_naturalGas = df[df.Product == 'NATURAL GAS'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    n = alt.Chart(df_product_naturalGas, title='Mean Price of Natural Gas Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = n.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = n.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_petrol_over_time_by_state(df):

    df_product_petrol = df[df.Product == 'PETROL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['State'], nearest=True)

    o = alt.Chart(df_product_petrol, title='Mean Price of Petrol Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = o.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = o.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_petrol_over_time_by_region(df):

    df_product_petrol = df[df.Product == 'PETROL'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    p = alt.Chart(df_product_petrol, title='Mean Price of Petrol Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = p.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = p.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_lpg_over_time_by_state(df):

    df_product_lpg = df[df.Product == 'LPG'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['State'], nearest=True)

    q = alt.Chart(df_product_lpg, title='Mean Price of LPG Over Time by State').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('State', legend=alt.Legend(
            title="State by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = q.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = q.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)

def mean_price_of_lpg_over_time_by_region(df):

    df_product_lpg = df[df.Product == 'LPG'].reset_index(drop=True)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Macroregion'], nearest=True)

    r = alt.Chart(df_product_lpg, title='Mean Price of Petrol Over Time by Region').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Macroregion', legend=alt.Legend(
            title="Macroregion by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = r.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = r.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)