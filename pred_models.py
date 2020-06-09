# coding=utf-8
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from preprocess import preprocess
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor


path = './2004-2019.tsv'
df = pd.read_csv(path, sep='\t', parse_dates=True)
df = preprocess(df)


def plt_linear_regression(df):
    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)

    X = df_product_diesel[['Year']].values
    y = df_product_diesel['Mean_Price'].values

    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std = sc_x.fit_transform(X)
    y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()

    slr = LinearRegression()
    slr.fit(X, y)
    y_pred = slr.predict(X)
    st.write('Slope: %.3f' % slr.coef_[0])
    st.write('Intercept: %.3f' % slr.intercept_)

    def lin_regplot(X, y, model):
        plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
        plt.plot(X, model.predict(X), color='black', lw=2)    
        return

    lin_regplot(X, y, slr)
    plt.xlabel('Year')
    plt.ylabel('Mean Price')

    #plt.show()
    st.pyplot()

def plt_decision_tree_regressor(df):
    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)

    X = df_product_diesel[['Year']].values
    y = df_product_diesel['Mean_Price'].values

    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std = sc_x.fit_transform(X)
    y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()

    def lin_regplot(X, y, model):
        plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
        plt.plot(X, model.predict(X), color='black', lw=2)    
        return

    tree = DecisionTreeRegressor(max_depth=3)
    tree.fit(X, y_std)

    sort_idx = X.flatten().argsort()

    lin_regplot(X[sort_idx], y_std[sort_idx], tree)
    plt.xlabel('Year')
    plt.ylabel('Mean_Price')

    st.pyplot()

def plt_ada_boost_regressor(df):
    df_product_diesel = df[df.Product == 'DIESEL'].reset_index(drop=True)

    X = df_product_diesel[['Year']].values
    y = df_product_diesel['Mean_Price'].values

    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std = sc_x.fit_transform(X)
    y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()

    def lin_regplot(X, y, model):
        plt.scatter(X, y, c='steelblue', edgecolor='white', s=70)
        plt.plot(X, model.predict(X), color='black', lw=2)    
        return

    regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=2),
                        n_estimators=20, random_state=42)
    regr_2.fit(X, y_std)

    sort_idx = X.flatten().argsort()

    lin_regplot(X[sort_idx], y_std[sort_idx], regr_2)
    plt.xlabel('Year')
    plt.ylabel('Mean_Price')

    st.pyplot()