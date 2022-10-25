import csv
import pandas as pd
import googlemaps

df = pd.read_excel(r'input.xlsx')
df.head()


gmaps_key = googlemaps.Client(key="your-key")


df["LatLong"] = df["Latitude"].astype(str) + "," + df["Longitude"].astype(str)
df

def geocode(add):
    g = gmaps_key.geocode(add)
    full_address = g[0]["formatted_address"]
    area = g[0]["address_components"][2]["short_name"]
    neighborhood = g[4]["address_components"][0]["short_name"]
    return (full_address, area, neighborhood)

df['geocoded'] = df['LatLong'].apply(geocode)
df['geocoded']

df.to_excel("output.xlsx")  

