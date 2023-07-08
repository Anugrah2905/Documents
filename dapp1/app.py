import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#loading the data

@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

#call the loaded data function

with st.spinner('loading data....'):
    df = load_data()

    #create title for your app

st.title('House price data analysis')

#display dataset

if st.checkbox('show dataset',True):
    st.subheader('dataset')
    st.dataframe(df)