# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw

# def scale_to_img(self, lat_lon):
     
#         # https://gamedev.stackexchange.com/questions/33441/how-to-convert-a-number-from-one-min-max-set-to-another-min-max-set/33445
#         old = (self.points[2], self.points[0])
#         new = (0, h_w[1])
#         y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
#         old = (self.points[1], self.points[3])
#         new = (0, h_w[0])
#         x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
#         # y must be reversed because the orientation of the image in the matplotlib.
#         # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
#         return int(x), h_w[1] - int(y)


# data_path = 'data.csv'
# data = pd.read_csv(data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')
# gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))

# image = Image.open('map.png', 'r')  # Load map image.
# img_points = []
# for d in gps_data:
#     x1, y1 = scale_to_img(d, (image.size[0], image.size[1]))  # Convert GPS coordinates to image coordinates.
#     img_points.append((x1, y1))
# draw = ImageDraw.Draw(image)
# draw.line(img_points, fill=(255, 0, 0), width=2)  # Draw converted records to the map image.

# image.save('resultMap.png')
# x_ticks = map(lambda x: round(x, 4), np.linspace(lon1, lon2, num=7))
# y_ticks = map(lambda x: round(x, 4), np.linspace(lat1, lat2, num=8))
# y_ticks = sorted(y_ticks, reverse=True)  # y ticks must be reversed due to conversion to image coordinates.

# fig, axis1 = plt.subplots(figsize=(10, 10))
# axis1.imshow(plt.imread('resultMap.png'))  # Load the image to matplotlib plot. 
# axis1.set_xlabel('Longitude')
# axis1.set_ylabel('Latitude')
# axis1.set_xticklabels(x_ticks)
# axis1.set_yticklabels(y_ticks)
# axis1.grid()
# plt.show()


import folium
import pandas
df=pandas.read_csv("data.csv")
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles="Stamen Terrain")
# def color(time):
#  minimum=int(min(df['TIME']))
#  step=int((max(df['TIME'])-min(df['TIME']))/3)
#  if elev in range(minimum,minimum+step):
#   col='green'
#  elif elev in range(minimum+step,minimum+step*2):
#   col='orange'
#  else:
#   col='red'
#  return col
fg=folium.FeatureGroup(name="EMPLOYEE LOCATIONS")
for lat,lon,name,time in zip(df['LAT'],df['LON'],df['NAME'],df['TIME']):
 fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name,time)),icon=folium.Icon(color='red',icon_color='green')))
map.add_child(fg)
# map.add_child(folium.GeoJson(data=open('datas.json')
# name="Population"
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save(outfile='map.html')