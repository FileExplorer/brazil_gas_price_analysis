#!/usr/bin/python3
import os
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
alt.data_transformers.disable_max_rows()

from start_screen import init_screen
from changes import show_changes
from translations import show_translations

from preprocess import preprocess
from data_exploration import count_observation_per_region, number_of_observation_by_state, number_of_gas_stations_per_state
from plots import mean_price_of_prod_over_time, mean_distrib_price_of_prod_over_time
from explore_products import mean_price_of_diesel_over_time_by_state, mean_price_of_diesel_over_time_by_region, mean_price_of_diesel_s10_over_time_by_state, mean_price_of_diesel_s10_over_time_by_region, mean_price_of_hydrous_ethanol_over_time_by_state, mean_price_of_hydrous_ethanol_over_time_by_region, mean_price_of_natural_gas_over_time_by_state, mean_price_of_natural_gas_over_time_by_region, mean_price_of_petrol_over_time_by_state, mean_price_of_petrol_over_time_by_region, mean_price_of_lpg_over_time_by_state, mean_price_of_lpg_over_time_by_region
from pred_models import plt_linear_regression, plt_decision_tree_regressor, plt_ada_boost_regressor


### STARTER ###

path = './2004-2019.tsv'

st.sidebar.header('Loading data.')

filename = st.sidebar.selectbox('Choose a file: ', ('None', '2004-2019'))

if filename is not "None":

    if len(filename.split(".")) == 1:

        filename = filename + '.tsv'

    try:
        
        df = pd.read_csv(path, sep='\t', parse_dates=True)

        st.title("Gas Prices in Brazil")

        st.header('Raw Data')

        st.write("To view raw data, click on the 'Display raw data + terminology' in the sidebar.")

        if st.sidebar.checkbox('Display raw data + terminology'):

            st.dataframe(df.head(10))

            if st.checkbox('Show column names'):

                st.dataframe(df.columns)

                if st.checkbox('Show column name translations'):

                    show_translations()               

    except:

        st.error("No such file could be found in the working directory.")

    st.header('Preprocessing')

    st.write("For our convenience, lets preprocess our data so that it is easier to look at. Click on the 'Preprocess' checkbox in the sidebar.")

    st.sidebar.subheader('Preprocess')

    if st.sidebar.checkbox('Preprocess'):

        df = preprocess(df)

        if st.checkbox('Show first 10 rows of preprocessed data'):

            st.dataframe(df.head(10))

            if st.checkbox('See changes'):

                show_changes()

### END ###

    ### DATA EXPLORATION ###

    st.sidebar.subheader('Data Exploration')

    if st.sidebar.checkbox('Count observations per Region'):

        count_observation_per_region(df)

    if st.sidebar.checkbox('Count observations per State'):

        number_of_observation_by_state(df)

    if st.sidebar.checkbox('State vs. Number of gas stations analyzed'):

        number_of_gas_stations_per_state(df)

    ### END ###

    
    ### TIME SERIES PLOT ###
        
    st.header('Data Exploration - Time Series Plot')

    something = st.selectbox('Select Time Series Plot', (
        'None', 'Mean Price of Products Over Time', 'Mean Distribution Price of Products Over Time'))

    if something == 'Mean Price of Products Over Time':
        mean_price_of_prod_over_time(df)

    elif something == 'Mean Distribution Price of Products Over Time':
        mean_distrib_price_of_prod_over_time(df)
    
    ### END ###


     ### EXPLORE PRODUCT ###

    st.sidebar.subheader('Explore Product')

    test = st.sidebar.selectbox('Select Product', ('None', 'DIESEL',
                                                   'DIESEL S10', 'HYDROUS ETHANOL', 'NATURAL GAS', 'PETROL', 'LPG'))

    if test == 'DIESEL':

        st.header("Diesel")
        mean_price_of_diesel_over_time_by_state(df)
        mean_price_of_diesel_over_time_by_region(df)

    elif test == 'DIESEL S10':

        st.header("Diesel S10")
        mean_price_of_diesel_s10_over_time_by_state(df)
        mean_price_of_diesel_s10_over_time_by_region(df)

    elif test == 'HYDROUS ETHANOL':

        st.header("Hydrous Ethanol")
        mean_price_of_hydrous_ethanol_over_time_by_state(df)
        mean_price_of_hydrous_ethanol_over_time_by_region(df)

    elif test == 'NATURAL GAS':

        st.header('Natural Gas')
        mean_price_of_natural_gas_over_time_by_state(df)
        mean_price_of_natural_gas_over_time_by_region(df)

    elif test == "PETROL":

        st.header('Petrol')
        mean_price_of_petrol_over_time_by_state(df)
        mean_price_of_petrol_over_time_by_region(df)

    elif test == 'LPG':

        st.header('LPG')
        mean_price_of_lpg_over_time_by_state(df)
        mean_price_of_lpg_over_time_by_region(df)

    ### END ###


    ### RUN PREDICTION MODEL ###

    st.header('Run Prediction Model')

    pred_selectbox = st.selectbox('Select prediction model', (
        'None', 'Linear Regression', 'Decision Tree Regressor', 'Ada Boost Regressor'))
    
    if pred_selectbox == 'Linear Regression':
        
        plt_linear_regression(df)
    
    elif pred_selectbox == 'Decision Tree Regressor':
        
        plt_decision_tree_regressor(df)
    
    elif pred_selectbox == 'Ada Boost Regressor':
        
        plt_ada_boost_regressor(df)

    ### END ###


   

else:

    ### START SCREEN ###

    init_screen()

    ### END ###