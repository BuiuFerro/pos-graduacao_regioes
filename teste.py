import geopandas as gpd
import plotly.graph_objects as go
import json

with open ("/home/brunoferro/Documents/mapa/Brasil.json") as response:
    mapa = json.load(response)

fig = go.Figure(go.Choroplethmapbox(geojson=mapa, colorscale="Viridis", zmin=0, zmax=12, marker_line_width=0))

fig.update_layout(mapbox_style="light", mapbox_zoom=3, mapbox_center = {"lat": -15.77972, "lon": -47.92972})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()