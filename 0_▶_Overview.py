#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:59:44 2022

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

st.set_page_config(
    page_title="X",
    page_icon="👋",
)

st.markdown(
    """
    # Spotify shuffler
    
    Spotify shuffler is an open-source app framework built to help you rediscover your music and own your playlists.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

