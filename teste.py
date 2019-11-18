import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
import json
from urllib.request import urlopen

with open("./Brasil.json") as response:
    mapa = json.load(response)
    
#with urlopen("https://dadosabertos.capes.gov.br/dataset/903b4215-ea91-4927-8975-d1484891374f/resource/0f1737bd-6227-4193-9d11-0f9e981e9789/download/br-capes-colsucup-prog-2018-2019-10-01.csv") as dados:
#    df = pd.read_csv(dados, error_bad_lines=False)

fig = go.Figure(go.Choroplethmapbox(geojson=mapa, colorscale="Viridis", zmin=0, zmax=12))

fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=4, mapbox_center = {"lat": -15.77972, "lon": -47.92972})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()