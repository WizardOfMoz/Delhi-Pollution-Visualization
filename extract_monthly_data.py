import pandas as pd
from folium.plugins import TimestampedGeoJson
import branca.colormap as cm
import pickle
pd.set_option('max_columns', 50)

pollution_df=pd.read_pickle('combined_data.pkl')
linear = cm.LinearColormap(['green', 'yellow', 'red'],vmin=0, vmax=500)
pollutants=['aqi','pm2.5cnc','pm10cnc']


def create_geojson_features(pollutant,month):
    global pollution_df
    global linear
    df=pollution_df[['deviceid','lat','lon','dt_time',pollutant]]
    df=df[df.dt_time.dt.month==month]
    df['color']=df[pollutant].apply(lambda row : linear(row))
    features = []
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[row['lon'],row['lat']]
            },
            'properties': {
                'time': row['dt_time'].strftime('%Y-%m-%d %H:%M:00'),
                'style': {'color' : row['color']},
                'icon': 'circle',
                'iconstyle':{
                    'fillColor': row['color'],
                    'fillOpacity': 0.8,
                    'stroke': 'true',
                    'radius': 7
                }
            }
        }
        features.append(feature)
    
    return features


for pollutant in pollutants:
    for month in range(1,13):
        features=create_geojson_features(pollutant,month)
        file_path='json_data/'+str(pollutant)+'_'+str(month)+'.pkl'
        print('> ',file_path)
        with open(file_path,'wb') as f:
            pickle.dump(features,f)
        
        


