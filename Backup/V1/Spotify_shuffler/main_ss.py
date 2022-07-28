#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:48:49 2022

@author: halimbouayad
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

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
import playlist_overview
from playlist_overview import *
username = "hyder14"


os.environ['SPOTIPY_CLIENT_ID'] = "fc99466410414fbb9aaafbfe76ab5a1d"
os.environ['SPOTIPY_CLIENT_SECRET'] = "83577093a17d4db3989a074b85b7905a"
os.environ['SPOTIPY_REDIRECT_URI'] = "http://localhost:1234"


# scope = "user-library-read"  
# token = SpotifyOAuth(scope=scope, username=username)
# spotifyObject = spotipy.Spotify(auth_manager=token)
# playlists = spotifyObject.current_user_playlists(limit=50)

# df=pd.DataFrame()   

# uris=[]
# names=[]
# tracks=[]

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#         uris.append(playlist['uri'])
#         names.append(playlist['name'])
#         tracks.append(playlist['tracks']['total'])
#     if playlists['next']:
#         playlists = spotifyObject.next(playlists)
#     else:
#         playlists = None


# df['name']=names
# df['tracks']=tracks





# http://127.0.01:5000/ is from the flask api




###### BELOW IS THE STREAMLIT PART




st.title('Spotify Playlist Shuffler')

st.text('The goal of this project is to gain better control of your playlists\n while exploring the features of the Spotify Web API.')


    
with st.expander('Create a playlist'):


    st.header('Create a playlist')
    st.write('Hello, *World!* :sunglasses:')
    
    scope = "playlist-modify-public"


    token = util.prompt_for_user_token(username,scope,client_id=os.environ['SPOTIPY_CLIENT_ID'],client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'])
    spotifyObject = spotipy.Spotify(auth=token)

    #spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)
    ################################################

    
    #create the playlist
    playlist_name = st.text_input('Enter a playlist name = ')
    playlist_description = st.text_input('Enter a playlist description = ')

    if st.button('Create playlist!'):
        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        spotifyObject = spotipy.Spotify(auth=token)
        spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)
    else:
        st.write('Have a great day') #displayed when the button is unclicked
last='Nothing yet, but you will see something when you click on a playlist.'


with st.expander('List of current playlists'):
    df=get_playlists(username)
    # st.header("List of playlist")
    
    # #if st.button('View playlist!'):
    # if 1==1:
    #     scope = "user-library-read"  
    #     token = SpotifyOAuth(scope=scope, username=username)
    #     spotifyObject = spotipy.Spotify(auth_manager=token)
    #     playlists = spotifyObject.current_user_playlists(limit=50)
    #     print('=================')
    #     #response = requests.get("http://localhost:1234", timeout=10)
    #     #print(response.json())
    #     print('=================')
    #     df=pd.DataFrame()   
        
    #     urls=[]
    #     names=[]
    #     tracks=[]
    #     links=[]
    #     ids=[]
        
    #     while playlists:
            
    #         for i, playlist in enumerate(playlists['items']):
    #             #print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    #             urls.append(playlist['uri'])
    #             names.append(playlist['name'])
    #             tracks.append(playlist['tracks']['total'])
    #             links.append(playlist['external_urls']['spotify'])
    #             ids.append(playlist['id'])
    #             #print(playlist)
    #             #st.text(last)
               
          
                
    #         if playlists['next']:
    #             playlists = spotifyObject.next(playlists)
    #         else:
    #             playlists = None
        
    #     #audio_analysis
        
    #     df['name']=names
    #     df['tracks']=tracks
    #     df['url']=urls
    #     df['id']=ids
    #     st.dataframe(df)   
        
    #     selected=st.selectbox('Please select to zoom', df.name)
            
    #     uri=df[df.name==selected].reset_index()['url'][0]
    #     #df_tracks=pd.DataFrame(playlist_content)
    #     playlist_content=spotifyObject.playlist(uri)
    #     names=[]
    #     releasedays=[]
    #     ids=[]
    #     for i,trax in enumerate(playlist_content['tracks']['items']):
        
    #         names.append(trax['track']['name'])
    #         #releasedays.append(trax['track']['added_at'])
    #         ids.append(trax['track']['id'])
            
    #     pl=pd.DataFrame()
    #     pl['name']=names
    #     #pl['release_date']=releasedays
    #     pl['id']=ids
    #     st.dataframe(pl)
    
        
with st.expander('What do your playlists look like?'):
        # st.header("EDA")
        # st.bar_chart(df.groupby('tracks').id.count())
        #print(df.url[len(df)-1])
        if isinstance(df, pd.DataFrame):
            EDA(df)
        
        
      
