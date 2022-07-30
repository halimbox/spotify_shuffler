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
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px

def EDA(df, st, features):
    #Key Metrics


    for i, feature in enumerate(features):
 
        temp=df.describe().loc['mean',:][feature]
        st.metric(feature, '{:.1%}'.format(temp))
    
    
df = pd.read_pickle('./spotify.pkl')  

     

def scatter(ds):

    
    fig = px.scatter(ds, x="energy", y="danceability", color="cluster",
                 size='track', template='plotly_dark', hover_data=['cluster_name'])
    
    return fig

def add_stats(ds):
    col1, col2=st.columns(2)
    EDA(ds, col1, features=['danceability','energy','acousticness'])
    EDA(ds, col2, features=['tempo','loudness','valence'])

def cluster(n, selected_features):
    
    from sklearn.cluster import KMeans
    

    all_features=['danceability',
           'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
           'instrumentalness', 'liveness', 'valence', 'tempo']

    X=df[selected_features]
    
    km = KMeans(
        n_clusters=n, init='random',
        n_init=10, max_iter=300, 
        tol=1e-04, random_state=0)
    
    clusters = km.fit_predict(X)
    
    df['cluster']=clusters
    
    
    stats=df.groupby('cluster').agg({'track':'count', 
                               'danceability':'mean',
                               'energy':'mean'}).reset_index()
    
    a, cluster_names = get_cluster_name(df, stats, 'yes', 'track', 1)

    print(cluster_names)
                                       
    stats['cluster_name']=cluster_names
    
    #for i in range(len(stats)):
   #     c=str(stats.index.values[i])
    #    stats.loc[i, 'cluster_name']=get_top_artists(df, c, 'artist', 3)
    print(stats)
    return stats, df

def get_cluster_name(df, stats, cluster, category, n_top):
    
    
    cluster_name = []
    for i in range(len(stats)):
                 
        if cluster!='':
            artists='#'+str(stats.loc[i,'cluster'])+' - '
            top=df[df.cluster==stats.loc[i,'cluster']].groupby(category).agg({'popularity':'min'}).sort_values(by='popularity',ascending=False).head(n_top).reset_index()[category].to_list()
        else:
            artists=''
    
            top=df.groupby(category).agg({'popularity':'min'}).sort_values(by='popularity',ascending=False).head(n_top).reset_index()[category].to_list()
            
            
        for i, artist in enumerate(top):
            if i == len(top)-2:
                artists+=artist+' & '
            elif i == len(top)-1:
                artists+=artist
            else:
                artists+=artist+', '
        cluster_name.append(artists)
    return artists, cluster_name

def create_playlist(df):
    st.title("Create Playlist")
    
    st.write('Generating a random playlist :smile:')
    
    
    
    with st.form('playlist_generate'):
        scope = "playlist-modify-public"
        
        
        n=1
        ds=df.sample(n)
        
 
        

        tab2, tab1 = st.tabs(['Clustering','Random selection'])
                             
        with tab1:                    

            slider_label='# of songs'
    
            n=st.slider(label=slider_label,min_value=1, max_value=30)
            submitted = st.form_submit_button("Generate random playlist")
            
            if submitted:
                ds=df.sample(n)
                st.write('Including songs from '+get_cluster_name(ds,ds,'','artist',3))
                st.dataframe(ds)
                add_stats(ds)
                with st.expander('Save Playlist'):
                    save_playlist()
        with tab2:
            slider_label='# of clusters'
            liste=df.columns.unique().to_list()
            n=st.slider(label=slider_label,min_value=1, max_value=30)
            selected_features = st.multiselect("Choose features to include", liste, [])
            submitted = st.form_submit_button("Generate rearranged playlist")
            if submitted:
                
                ds, df =cluster(n,selected_features)
          
                
                
                #add_stats(ds)
                selected_cluster=st.selectbox('Select cluster to zoom', ds.reset_index().cluster_name.unique())
                
                if selected_cluster:
                    k=ds[ds.cluster_name==selected_cluster].index.values[0]
             
                    st.dataframe(df[df.cluster==k])
                    
                    st.plotly_chart(scatter(ds), use_container_width=True)
                    #st.dataframe(ds)
                
                with st.expander('Save Playlist'):
                    save_playlist()
        
        
def save_playlist():
    with st.container():
        playlist_name = st.text_input('Enter a playlist name = ')
        playlist_description = st.text_input('Enter a playlist description = ')
        
        if st.form_submit_button(label='Save playlist!'):
            token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
            spotifyObject = spotipy.Spotify(auth=token)
            spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)
   

create_playlist(df)


import seaborn as sns 
ds, df = cluster(8,['danceability','energy'])
