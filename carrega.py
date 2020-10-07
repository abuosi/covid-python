import pandas as pd
import folium
import datetime

br_states = "Brasil.json"
covid_dataset = pd.read_csv("brasil-total.csv", low_memory=False, sep=';')

# Calculate Yesterday Date
yesterday = datetime.date.today() - datetime.timedelta(days=1)

covid_dataset['casosMilhao'] = round((covid_dataset['casosAcumulado']*1000000)/covid_dataset['populacaoTCU2019'])
covid_dataset['obitosMilhao'] = round((covid_dataset['obitosAcumulado']*1000000)/covid_dataset['populacaoTCU2019'])
# filter
filter_states = pd.notnull(covid_dataset["estado"]) & pd.isnull(covid_dataset["municipio"]) & pd.isnull(covid_dataset["codmun"]) & (covid_dataset["data"] == yesterday.strftime('%Y-%m-%d'))
covid_filtered = covid_dataset[filter_states]

m = folium.Map([-15.925556, -47.570433], zoom_start=4)

folium.Choropleth(
    geo_data=br_states,
    data=covid_filtered,
    columns=['estado', 'casosMilhao'],
    key_on='feature.properties.UF',
    fill_color='OrRd'
).add_to(m)

m.save('mapa.html')
