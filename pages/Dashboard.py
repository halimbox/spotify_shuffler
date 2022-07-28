#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:48:49 2022

@author: halimbouayad
"""

import pandas as pd
import numpy as np


from datetime import datetime 
import os

# #load data

# dir = os.getcwd()
# path = os.path.join(dir, 'data.csv')

# try:
#     df=pd.read_csv(path)
#     df_continent=pd.DataFrame(df.groupby('continent').total_deaths.sum())
# except:
#     print('Error has occured')


    
    
# ################################################

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from requests import *
import pandas as pd
import streamlit as st

import sys
  
# Custom imports

username = "hyder14"


def EDA(df, st, features):
    #Key Metrics

    
    
    for i, feature in enumerate(features):
 
        temp=df.describe().loc['mean',:][feature]
        st.metric(feature, '{:.1%}'.format(temp))
    
    
    st.text('Top songs from that album:')
    st.dataframe(dff)

    selected=st.selectbox('By playlist (click to select other filter)', df.columns)
    st.bar_chart(df[df.playlist==f_value].groupby(selected).agg({'danceability':'mean'}))
 
    
     



st.title('Dashboard')
st.write('Pick a playlist to view detailed stats')
df = pd.read_pickle('./spotify.pkl')
f_value=st.selectbox('Select a playlist', df.playlist.unique())
dff=df[df.playlist==f_value]
col1, col2 = st.columns(2)

# col1.header("Create playlist)

# col1.write('Hello, *World!* :sunglasses:')

# scope = "playlist-modify-public"


# playlist_name = col1.text_input('Enter a playlist name = ')
# playlist_description = col1.text_input('Enter a playlist description = ')

# if col1.button('Create playlist!'):
#     token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
#     spotifyObject = spotipy.Spotify(auth=token)
#     spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)




EDA(df, col1, features=['danceability','energy','acousticness'])
EDA(df, col2, features=['tempo','loudness','valence'])
    

           
