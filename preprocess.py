# coding=utf-8

import os
import pandas as pd
import numpy as np


path = './2004-2019.tsv'
df = pd.read_csv(path, sep='\t', parse_dates=True)

def preprocess(df):
    # Rename column headers
    df.columns = ["Unnamed:_0",
                    "Analysis_Date",
                    "Last day of analyses of week",
                    "Macroregion",
                    "State",
                    "Product",
                    "No of Gas Stations Analyzed",
                    "Measurement unit",
                    "Mean Price",
                    "Std Dev",
                    "Min Price",
                    "Max Price",
                    "Mean Price Margin",
                    "Coefficient of variation",
                    "Mean Dist Price",
                    "Distribution Std Dev",
                    "Distribution Min Price",
                    "Distribution Max Price",
                    "Distribution Coefficient of Variation",
                    "Month",
                    "Year"]

    # Drop useless column
    df = df.drop(columns=['Unnamed:_0'])

    # Replace whitespace with underscore
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.replace("'", "")
    df.columns = df.columns.str.replace("Distribution", "Dist")

    # Correct dtypes
    float_columns = ['Mean_Price_Margin', 'Mean_Dist_Price', 'Dist_Std_Dev',
                        'Dist_Min_Price', 'Dist_Max_Price',
                        "Dist_Coefficient_of_Variation"]

    # Replace "-" with 0 in order to convert to float
    for column in float_columns:
        df[column] = df[column].str.replace("-", "0")

    # Fill nulls and convert to float
    df[float_columns] = df[float_columns].fillna(0).astype(float)

    # Rename Product categories
    products = {"ÓLEO DIESEL": "DIESEL", "GASOLINA COMUM": "PETROL", "GLP": "LPG",
                "ETANOL HIDRATADO": "HYDROUS ETHANOL", "GNV": "NATURAL GAS", "ÓLEO DIESEL S10": "DIESEL S10"}

    df["Product"] = df.Product.map(products)

    # Rename Measurement_unit categories
    units = {"R$/l": "liter", "R$/13Kg": "13kg", "R$/m3": "m3"}

    df["Measurement_unit"] = df["Measurement_unit"].map(units)

    # Create Year_Month column for time series plots
    year_month = df.Year.astype(str) + "-" + df.Month.astype(str)
    df["Year_Month"] = pd.to_datetime(year_month)
    return df





