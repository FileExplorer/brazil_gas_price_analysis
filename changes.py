# coding=utf-8
import streamlit as st


def show_changes():
    st.subheader('Changes')
    st.write(" - Translated and changed the name of the column headers")
    st.write(" - Dropped the **Unnamed:_0** column")
    st.write(" - Replaced whitespaces with underscore")
    st.write(" - Corrected data types")
    st.write(" - Replaced '-' with 0 in order to convert to float")
    st.write(" - Filled NA's")
    st.write(" - Renamed Product categories")
    st.write(" - Fixed Measurement Unit category")
    st.write(" - Created Year_Month column")