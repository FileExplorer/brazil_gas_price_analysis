# coding=utf-8
import streamlit as st


def show_translations():
    st.subheader('Terminology')
    st.write('- DATA INICIAL or start date: Date of start the collection of data')
    st.write('- DATA FINAL or end date: Date of end the collection of data')
    st.write('- REGIÃO or region: Is a subdivision of Brazil. There are 5 Region: Sul - South, Sudeste - Southeast, Centro-Oeste - Midwest, Nordeste - Northeast e Norte - North.')
    st.write('- ESTADO or states: Brazil has 26 states and one federal district')
    st.write(' - PRODUTO or fuel: There are 6 types of fuel: Óleo diesel - Diesel, Gasolina comum - Regular gasoline, GLP - LPG, Etanol hidratado - Hydrous Ethanol, GNV - Natural gas e Óleo Diesel S10 - Diesel S10')
    st.write(' - NÚMERO DE POSTOS PESQUISADOS or number of gas stations: Number of gas stations consulted in the research')
    st.write(' - UNIDADE DE MEDIDA or unit: Unit about each fuel in the research.')
    st.write(' - PREÇO MÉDIO REVENDA or avarege price of resale: Average price of resale in each collection')
    st.write(' - DESVIO PADRÃO REVENDA or standard deviation price of resale: Standard deviation price of resale in each collection')
    st.write(' - PREÇO MÍNIMO REVENDA or minimum price of resale: Minimum price of resale in each collection')
    st.write(' - PREÇO MÁXIMO REVENDA or maximum price of resale: Maximum price of resale in each collection')
    st.write(' - MARGEM MÉDIA REVENDA or average amount for profit of resale: Average of profit in release in reach collection')
    st.write(' - ANO or year: Year of each collection')
    st.write(' - MÊS or month: Month of each collection')
    st.write(' - COEF DE VARIAÇÃO DISTRIBUIÇÃO or coefficient of variation about distribution: coefficient of variation about distribution of each colection')
    st.write(' - PREÇO MÁXIMO DISTRIBUIÇÃO or maximum price of distribution: Maximum price of distribution in each collection')
    st.write(' - REÇO MÍNIMO DISTRIBUIÇÃO or minimum price of ditribution: Minimum price of distribution in each collection')
    st.write(' - DESVIO PADRÃO DISTRIBUIÇÃO or standard deviation price of distribution: Standard deviation price of resale in each collection')
    st.write(' - PREÇO MÉDIO DISTRIBUIÇÃO or average price of distribution: Average price of distribution in each collection')
    st.write(' - COEF DE VARIAÇÃO REVENDA or coefficient of variation about resale: coefficient of variation about resale of each colection') 