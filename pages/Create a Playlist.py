#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:57:31 2022

@author: halimbouayad
"""


import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from requests import *
import pandas as pd
import streamlit as st
def EDA(df, st, features):
    #Key Metrics


    for i, feature in enumerate(features):
 
        temp=df.describe().loc['mean',:][feature]
        st.metric(feature, '{:.1%}'.format(temp))
    
    
df = pd.read_pickle('./spotify.pkl')  

     


def create_playlist(df):
    st.title("Create Playlist")
    
    st.write('Generating a random playlist :smile:')
    
    scope = "playlist-modify-public"
    
    ds=df.sample(5)
    
    if st.button('Refresh Playlist!'):
        ds=df.sample(5) 
    
    st.dataframe(ds)

    col1, col2=st.columns(2)
    EDA(ds, col1, features=['danceability','energy','acousticness'])
    EDA(ds, col2, features=['tempo','loudness','valence'])
    
    playlist_name = st.text_input('Enter a playlist name = ')
    playlist_description = st.text_input('Enter a playlist description = ')
    
    if st.button('Save playlist!'):
        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        spotifyObject = spotipy.Spotify(auth=token)
        spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

 
create_playlist(df)


    