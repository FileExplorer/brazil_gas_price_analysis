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


def mean_price_of_prod_over_time(df):
    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)
    df_product_petrol = df[df.Product == 'PETROL'].reset_index(drop=True)
    df_product_naturalGas = df[df.Product ==
                                'NATURAL GAS'].reset_index(drop=True)
    df_product_hydrousEthanol = df[df.Product ==
                                    'HYDROUS ETHANOL'].reset_index(drop=True)
    df_product_diesels10 = df[df.Product ==
                                'DIESEL S10'].reset_index(drop=True)

    frames = [df_product_diesel, df_product_petrol, df_product_naturalGas,
                df_product_hydrousEthanol, df_product_diesels10]
    result = pd.concat(frames)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Product'], nearest=True)

    f = alt.Chart(result, title='Mean Price of Products Over Time').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Price)',
        color=alt.Color('Product', legend=alt.Legend(
            title="Product by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = f.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = f.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)


def mean_distrib_price_of_prod_over_time(df):
    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)
    df_product_petrol = df[df.Product == 'PETROL'].reset_index(drop=True)
    df_product_naturalGas = df[df.Product ==
                                'NATURAL GAS'].reset_index(drop=True)
    df_product_hydrousEthanol = df[df.Product ==
                                    'HYDROUS ETHANOL'].reset_index(drop=True)
    df_product_diesels10 = df[df.Product ==
                                'DIESEL S10'].reset_index(drop=True)

    frames = [df_product_diesel, df_product_petrol, df_product_naturalGas,
                df_product_hydrousEthanol, df_product_diesels10]
    result = pd.concat(frames)

    highlight = alt.selection(type='single', on='mouseover',
                                fields=['Product'], nearest=True)

    g = alt.Chart(result, title='Mean Distribution Price of Products Over Time').mark_line().encode(
        x='Year_Month',
        y='mean(Mean_Dist_Price)',
        color=alt.Color('Product', legend=alt.Legend(
            title="Product by color"))
    ).properties(
        width=1000,
        height=400
    )

    points = g.mark_line().encode(
        opacity=alt.value(0)
    ).add_selection(
        highlight
    ).properties(
        width=600
    )

    lines = g.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3))
    )

    st.altair_chart(points + lines)