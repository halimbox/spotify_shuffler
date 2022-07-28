#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:15:02 2022

@author: halimbouayad
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from requests import *
import pandas as pd
import streamlit as st

st.header("List of playlist")

#if st.button('View playlist!'):
def get_playlists(username):
    scope = "user-library-read"  
    token = SpotifyOAuth(scope=scope, username=username)
    spotifyObject = spotipy.Spotify(auth_manager=token)
    playlists = spotifyObject.current_user_playlists(limit=50)
    print('=================')
    #response = requests.get("http://localhost:1234", timeout=10)
    #print(response.json())
    print('=================')
    df=pd.DataFrame()   
    
    urls=[]
    names=[]
    tracks=[]
    links=[]
    ids=[]
    
    while playlists:
        
        for i, playlist in enumerate(playlists['items']):
            #print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
            urls.append(playlist['uri'])
            names.append(playlist['name'])
            tracks.append(playlist['tracks']['total'])
            links.append(playlist['external_urls']['spotify'])
            ids.append(playlist['id'])
            #print(playlist)
            #st.text(last)
           
      
            
        if playlists['next']:
            playlists = spotifyObject.next(playlists)
        else:
            playlists = None
    
    #audio_analysis
    
    df['name']=names
    df['tracks']=tracks
    df['url']=urls
    df['id']=ids
    st.dataframe(df)   
    
    selected=st.selectbox('Please select to zoom', df.name)
        
    uri=df[df.name==selected].reset_index()['url'][0]
    #df_tracks=pd.DataFrame(playlist_content)
    playlist_content=spotifyObject.playlist(uri)
    names=[]
    releasedays=[]
    ids=[]
    for i,trax in enumerate(playlist_content['tracks']['items']):
    
        names.append(trax['track']['name'])
        #releasedays.append(trax['track']['added_at'])
        ids.append(trax['track']['id'])
        
    pl=pd.DataFrame()
    pl['name']=names
    #pl['release_date']=releasedays
    pl['id']=ids
    st.dataframe(pl)
    return df 

def EDA(df):
    st.header("EDA")
    st.bar_chart(df.groupby('tracks').id.count())