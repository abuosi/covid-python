import pandas as pd
import folium
import datetime

covid = pd.read_csv("https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/master/data/Bing-COVID19-Data.csv", low_memory=False)

# polygons of the states of Brazil
br_states = "Brasil.json"

# dataset of Brazil population
population = pd.read_csv("populacao2020.csv", low_memory=False, sep=";")

# Calculate Yesterday Date
yesterday = datetime.date.today() - datetime.timedelta(days=1)

filter_states = pd.notnull(covid["AdminRegion1"]) & pd.isnull(covid["AdminRegion2"]) & (covid["Country_Region"] == "Brazil") & (covid["Updated"] == yesterday.strftime('%m/%d/%Y'))

# apply filter in dataset
covid = covid[filter_states]

# merge of population in main dataset
covid = covid.merge(population, right_on='Estado', left_on='AdminRegion1')
del covid['Estado']

# incidence calculation of cases and deaths
covid['confirmedMillion'] = round((covid['Confirmed']*1000000)/covid['Populacao'])
covid['deathsMillion'] = round((covid['Deaths']*1000000)/covid['Populacao'])

# save to csv
# covid.to_csv('base.csv')

m = folium.Map([-15.925556, -47.570433], zoom_start=4)

folium.Choropleth(
    geo_data=br_states,
    data=covid,
    columns=['UF', 'confirmedMillion'],
    key_on='feature.properties.UF',
    fill_color='OrRd'
).add_to(m)

m.save('mapa.html')


