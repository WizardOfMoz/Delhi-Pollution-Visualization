from flask import Flask,request
import pickle
import folium
from folium.plugins import TimestampedGeoJson

app=Flask(__name__)

def make_map(features):
    print('> Making map...')
    pollution_map = m = folium.Map(location=[28.630691, 77.217648], zoom_start=12, tiles='cartodbpositron')

    TimestampedGeoJson(
        {'type': 'FeatureCollection',
        'features': features}
        , period='PT6H'
        , duration='PT6H'
        , add_last_point=False
        , loop=False
        , max_speed=1
        , loop_button=True
        , time_slider_drag_update=True
    ).add_to(pollution_map)
    print('> Done.')
    return pollution_map

@app.route('/', methods=['GET', 'POST'])
def init():
    pollutant = str(request.args.get('pollutant','aqi'))
    month=int(request.args.get('month',10))
    period=str(request.args.get('period','P1D'))
    
    file_path='json_data/'+str(pollutant)+'_'+str(month)+'.pkl'
    print(file_path)
    f=open(file_path,'rb')
    features=pickle.load(f)
    
    print('> Making map...')
    pollution_map=make_map(features)
    return pollution_map._repr_html_()


if __name__=='__main__':
    app.run()



