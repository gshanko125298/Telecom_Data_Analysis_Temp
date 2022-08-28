#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("Telecom_Data_Analysis_Temp")

    df_satisf = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_score = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\user_Involvment_upadated.csv")

    st.header("Top 10 Satisfied Customers")
    st.dataframe(df_satisf)
    st.bar_chart(df_satisf['User_satisfaction_score'])

    st.subheader("Score Table")
    st.dataframe(df_score)
    st.bar_chart(df_score['User_satisfaction_score'])

    st.header("User Clustering based uasage of the user")
    st.image('data/satisfaction.png')
    st.markdown(
        'By Raising the **experience score**, we can improve user satisfaction.')

