#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import yfinance as yf
import datetime as dt
from plotly import graph_objs as go
#from multipage import MultiPage
import joblib


# 

# In[8]:


start = dt.datetime(2015,1,1)
end = dt.datetime.now()


st.title("Cryptocurrency prediction App")
coins = ('Bitcoin','Ethereum','Tether','Binance Coin','USD Coin','XRP','Solana','Terra','Cardano',
               'Avalanche','HEX','Dogecoin','Polkadot','TerraUSD','Binance USD','SHIBA INU','Wrapped Bitcoin',
               'NEAR Protocol','Polygon','Crypto.com','Dai','Litecoin','Cosmos','Chainlink','Uniswap','Wrappped TRON',
               'TRON','Bitcoin Cash','Lido stETH','FTX Token','UNUS SED LEO','Algorand','Stellar','Ethereum Classic',
               'Monero')
#period = ('day':1, 'week':7, 'month':30, 'quarter':90)
selected_coin = st.selectbox("select dataset for prediction", coins)
#n-period = st.selectbox("select time to predict", period)
n_period = st.slider("select time to predict", 1,3)
period= n_period * 30

# @st.cache
# def load_data(ticker):
#     data = yf.download(ticker, start,end)
#     data.reset_index(inplace= True)


# In[16]:


get_ipython().system('jupyter nbconvert   --to script gui_streamlit.ipynb')
get_ipython().system("awk '!/ipython/' gui_streamlit.py >  temp.py && mv temp.py app.py && rm gui_streamlit.py")
get_ipython().system('streamlit run app.py')


# In[ ]:


jupyter nbconvert –to script JupyterNotebookName.ipynb
awk ‘!/ipython/’ JupyterNotebookName.py > temp.py && mv temp.py app.py && rm JupyterNotebookName.py
streamlit run app.py

