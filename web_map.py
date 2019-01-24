import folium
import pandas as pd


def color_by_elev(elev):
    color = "blue"
    if elev <1000:
        color='green'
    elif (elev > 2000) & (elev < 3000):
        color='orange'
    elif(elev > 3000):
        color = 'red'
    return color


volcanoes = pd.read_csv("Volcanoes.txt")
lat = volcanoes.LAT
lon = volcanoes.LON
pu = volcanoes.NAME
elev = volcanoes.ELEV

pu_string = '''
NAME:  {}<br>
ELEVATION: {}<br>
<a href="https://www.google.com/search?q={}+volcano" target="_blank">{}</a><br>
'''
map= folium.Map(location=[39.9,-105.1],zoom_start=6)
fg = folium.FeatureGroup(name='Volcanoes')
for lat1,lon1,name,elev1 in zip(lat,lon,pu,elev):
    iframe = folium.IFrame(html=pu_string.format(name,elev1,name,name),width=300,height=100)
    # tempString = pu1 + " is " + str(elev1) + " meters above sea level"
    fg.add_child(folium.CircleMarker(radius=5, location=[lat1,lon1],popup=folium.Popup(iframe), color='grey', fill_opacity=0.7, fill_color=color_by_elev(elev1)))

# fg.add_child(folium.Marker(location=[39.,-105.1],popup='This is a sweet spot',icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[39.3,-105.3],popup='This is a sweet spot',icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Denver_advanced.html")

print('shit')

