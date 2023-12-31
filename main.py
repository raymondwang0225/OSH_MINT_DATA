import streamlit as st
from typing import List
from dataclasses import dataclass
from itertools import product
import json;
from PIL import Image
import requests
import pandas as pd
import numpy as np
import csv
import plost
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("OSH(orc-cash) Holding Data")


OSH_LIST_HOLDERS =pd.read_csv('OSH_LIST_HOLDERS_CSV.csv')


#row size 35 px
st.dataframe(OSH_LIST_HOLDERS,height=630,use_container_width =True,column_config={
        "Holding %": st.column_config.ProgressColumn(
            "Holding %",
            width = "large",
            help="Show Holding Percentage",
            format=" %.4f%%",
            min_value=0,
            max_value=10,
        ),
        "Rank": st.column_config.Column(
            "Rank",
            width = "small",
            help="Show rank order",
        ),
    },hide_index=True,)
