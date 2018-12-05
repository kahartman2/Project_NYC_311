import requests
import pandas as pd
import json

open_nyc = requests.get('https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$limit=9000000').json()
open_nyc_df = pd.DataFrame.from_records(open_nyc)
open_nyc_df.to_csv('open_nyc_data')
