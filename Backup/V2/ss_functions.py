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

def connect(scope, username):
    scope = "user-library-read"  
    token = SpotifyOAuth(scope=scope, username=username)
    spotifyObject = spotipy.Spotify(auth_manager=token)
    return spotifyObject


def get_data(sp, username):
    playlists = sp.current_user_playlists(limit=50)
    
    tr_names=[]
    pl_urls=[]
    pl_names=[]
    #tracks=[]
    #links=[]
    ids=[]
    
    while playlists:
        
        for i, playlist in enumerate(playlists['items']):
            #print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
            # urls.append(playlist['uri'])
            # names.append(playlist['name'])
            # tracks.append(playlist['tracks']['total'])
            # links.append(playlist['external_urls']['spotify'])
            # ids.append(playlist['id'])
            #print(playlist)
            #st.text(last)
            
            for i,trax in enumerate(playlist_content['tracks']['items']):
                
                tr_names.append(trax['track']['name'])
                #releasedays.append(trax['track']['added_at'])
                ids.append(trax['track']['id'])
                pl_names.append(playlist['name'])
                pl_urls.append(playlist['uri'])
            
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    
    #audio_analysis
    
    df['playlist']=pl_names
    df['track']=tr_names
    df['playlist_url']=pl_urls
    df['track_id']=ids
    st.dataframe(df)   

def playlist_details(sp, df, username):
    
   
    
    selected=st.selectbox('Please select to zoom', df.name)
    uri=df[df.name==selected].reset_index()['url'][0]
    #df_tracks=pd.DataFrame(playlist_content)
    
    # Connection to Spotipy
    #sp=connect(scope='user-library_read', username=username)
    playlist_content=sp.playlist(uri)
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
    
#if st.button('View playlist!'):
    
def playlist_overview(sp, username):
    # scope = "user-library-read"  
    # token = SpotifyOAuth(scope=scope, username=username)
    # spotifyObject = spotipy.Spotify(auth_manager=token)
    
    
    playlists = sp.current_user_playlists(limit=50)
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
            playlists = sp.next(playlists)
        else:
            playlists = None
    
    #audio_analysis
    
    df['name']=names
    df['tracks']=tracks
    df['url']=urls
    df['id']=ids
    st.dataframe(df)   
    