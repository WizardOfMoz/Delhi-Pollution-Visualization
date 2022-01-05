## Instructions
1. plot_heatmap.ipynb contains the code for end to end plotting of data.
2. extract_monthly_data.py is the pipeline for data where the geojson features are pickled
3. app.ipynb is the notebook for what is eventually being done in app.py
4. app.py is the flask application for rendering the map on web.

for calling the endpoints of app.py use the following format-
http://127.0.0.1:5000/?pollutant={pollutant}&month={month_number}&period={period according to format defined in app.ipynb}

Eg- http://127.0.0.1:5000/?pollutant=aqi&month=10&period=P1D

### It must be noted that while the same things are being done in app.py and app.ipynb the timebar does not work on the former.

