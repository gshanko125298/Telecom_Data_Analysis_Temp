#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("Telecom_Data_Analysis_Temp")

    df_avgThr = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_rtt = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tcp = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_frqThr = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_frqrtt = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_frqtcp = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")

    st.header("Top 10 Telcom Users Experience analysis")
    st.subheader("Average Throughput")
    st.dataframe(df_avgThr)
    st.bar_chart(df_avgThr['Average throughput'])

    st.subheader("Round Trip Time")
    st.dataframe(df_rtt)
    st.bar_chart(df_rtt['Average RTT'])

    st.subheader("TCP")
    st.dataframe(df_tcp)
    st.bar_chart(df_tcp['Average TCP'])

    st.header("Most Frequenct Users")
    st.subheader('Frquent Average Throughput')
    st.dataframe(df_frqThr)
    st.bar_chart(df_frqThr['0'])

    st.subheader("Frquent Round Trip Time")
    st.dataframe(df_frqrtt)
    st.bar_chart(df_frqrtt['0'])

    st.subheader("Frquent TCP")
    st.dataframe(df_frqtcp)
    st.bar_chart(df_frqtcp['0'])

    st.header("Cluster with 3 Group Classification")
    st.image('data/clusterExp.png')

