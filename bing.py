import pandas as pd
import folium
import datetime

covid = pd.read_csv("https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/master/data/Bing-COVID19-Data.csv", low_memory=False)

covid.dtypes

