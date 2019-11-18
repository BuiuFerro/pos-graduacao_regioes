import pandas as pd
import plotly.graph_objects as go
import json

with open("./Brasil.json") as response:
    mapa = json.load(response)
    
df = pd.read_csv("https://dadosabertos.capes.gov.br/dataset/903b4215-ea91-4927-8975-d1484891374f/resource/0f1737bd-6227-4193-9d11-0f9e981e9789/download/br-capes-colsucup-prog-2018-2019-10-01.csv",
                 encoding='latin-1', sep=';')

fig = go.Figure(go.Choroplethmapbox(geojson=mapa, colorscale="Viridis", zmin=0, zmax=12, marker_opacity=0.5, marker_line_width=0, locations=df_uf))

fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=4, mapbox_center = {"lat": -15.77972, "lon": -47.92972})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.show()