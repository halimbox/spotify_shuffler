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

import ss_functions
from ss_functions import *
import env_variables
# Custom imports



username = "hyder14"






st.title('List of playlist')




if st.button('Refresh playlists'):
    sp=connect(scope='user-library_read', username=username)
    df, test=get_data(sp, username)
    df.to_pickle('./spotify.pkl')
    print(df.columns)
    print('---------')
    if isinstance(df, pd.DataFrame):
        st.write('Dataframe has been successfuly saved!')
        code = '''df.to_pickle('./spotify.pkl')\nprint(df.columns)'''
        
        st.code(code, language='python')
      
        st.code(df.columns[:])
    
else:
    df = pd.read_pickle('./spotify.pkl')
st.dataframe(df)

    

    

           
