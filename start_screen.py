# coding=utf-8
import streamlit as st
from PIL import Image

def init_screen():
    st.header('**Gas Prices in Brazil: Exploratory Data Analysis (EDA)**')

    img = Image.open('./gas_station.jpg')
    st.image(img, use_column_width=True)

    st.subheader('The Data')
    st.write('The National Agency of Petroleum, Natural Gas and Bio fuels (ANP in Portuguese) releases weekly reports of gas, diesel and other fuels prices used in transportation across the country. These datasets bring the mean value per liter, number of gas stations analyzed and other information grouped by regions and states across the country.')
    st.subheader('Source')
    st.write('As stated before, these datasets are provided by ANP, and are regularly updated with new dates and information - which can be retrieved here (in portuguese).')
    st.subheader('What can be done with this?')
    st.write(" - How different regions of Brazil saw their gas prices change? \n")
    st.write(" - Within a region, which states increased more their prices? \n")
    st.write(" - Which states are the cheapest (or most expensive) for different types of fuels? \n")