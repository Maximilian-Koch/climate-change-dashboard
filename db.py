import sqlite3
import pandas as pd
import os

#else might look for databases in wrong directory, depending on IDE as well
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'climate.db')
conn = sqlite3.connect(db_path, check_same_thread=False)

def get_data(country,framing):
    #shown statistics depend on the chosen pill
    pos = ('RENEWABLE_ENERGY', 'POLICY_NUMBER', 'EMISSIONS', 'AREAS')
    neg = ('SURFACE_TEMP', 'FOSSIL_FUEL', 'DISASTER_FREQUENCY', 'DROUGHTS')
    #get ISO3 code of country name
    iso3 = pd.read_sql_query("SELECT * FROM countries \nWHERE country_names='{}';".format(country),conn)['ISO3'][0]
    #get data for country
    data = pd.read_sql_query("SELECT * FROM statistics \nWHERE ISO3='{}' AND stat IN {};".format(iso3, eval(framing)),conn)
    data['Value'] = data['Value'].fillna('null')
    output = []
    #seperate data into a dictionary, so that it can be converted into JSON for chart.js
    for stat in eval(framing):
        mask = data[data['stat']==stat]
        coords = {'x' : list(mask['Year']), 'y' : list(mask['Value'])}
        output.append(coords)
    return output

