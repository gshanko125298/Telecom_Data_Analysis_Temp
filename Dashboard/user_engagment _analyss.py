#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("Telecom_Data_Analysis_Temp")

    df_tele_email = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_game = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_google = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_netflix = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_otherAct = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_social = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_youtube = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_session = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")
    df_tele_DLUL = pd.read_csv("C:\Users\Genet Shanko\Telecom_Data_Analysis_Temp\Data\Week1_challenge_data_source(CSV).csv")

    st.header("Top 3 best Handset Manufacturers of the telcom")
    st.image('data/3_best_handset_manufacturers.png')

    st.header("Top 5 best Handsets used for communication")
    st.image('data/5 best phones used in communication.png')
    
    st.header("Data transfers and overall data usage correlation.")
    st.image('data/corellation.png')
    st.markdown(
        'There is a correlation between data transfers and total data usage in games and other apps.')

    st.header("Top 10 Users Engaged Per Application")
    st.subheader("Email App users")
    st.dataframe(df_tele_email)
    st.bar_chart(df_tele_email.Email_Total_Data)

    st.subheader("Game App users")
    st.dataframe(df_tele_game)
    st.bar_chart(df_tele_game.Gaming_Total_Data)

    st.subheader("Google App users")
    st.dataframe(df_tele_google)
    st.bar_chart(df_tele_google.Google_Total_Data)

    st.subheader("Netflix App users")
    st.dataframe(df_tele_netflix)
    st.bar_chart(df_tele_netflix.Netflix_Total_Data)

    st.subheader("Other App users")
    st.dataframe(df_tele_otherAct)
    st.bar_chart(df_tele_otherAct.Other_Total_Data)

    st.subheader("Social Media App users")
    st.dataframe(df_tele_social)
    st.bar_chart(df_tele_social.Social_Media_Total_Data)

    st.subheader("Youtube App users")
    st.dataframe(df_tele_youtube)
    st.bar_chart(df_tele_youtube.Youtube_Total_Data)

    st.subheader("Top 10 users based on session count")
    st.dataframe(df_tele_session)
    st.bar_chart(df_tele_session['Dur. (ms)'])

    st.subheader("Top 10 users based on download and upload count")
    st.dataframe(df_tele_DLUL)
    st.bar_chart(df_tele_DLUL['Total UL and DL'])

    st.header("3 groups k-means clustering")
    st.image('data/engclusters.png')

