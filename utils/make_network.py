import requests
import zipfile
import io
import pandas as pd
import geopandas as gpd
from shapely import Point


def create_census_geoid(lion_in: pd.DataFrame) -> pd.DataFrame:
    # This function converts the hierarchical census codes of county (borough), census-tract, and census-block to a single census 'geo_ID'
    Boro_Code = lion_in["Boro"].astype(int).astype(str)
    Boro_Code.loc[Boro_Code == "1"] = "061"
    Boro_Code.loc[Boro_Code == "2"] = "005"
    Boro_Code.loc[Boro_Code == "3"] = "047"
    Boro_Code.loc[Boro_Code == "4"] = "081"
    Boro_Code.loc[Boro_Code == "5"] = "085"
    Tract = lion_in["CT2020"].str.replace(" ", "0")
    Tract_Suf = lion_in["CT2020Suf"].str.replace(" ", "0")
    Block_Code = lion_in["CB2020"].str[0]

    geo_ID = Boro_Code + Tract + Tract_Suf + Block_Code

    return geo_ID


def gtfs_mta_import(url: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    # Pull in regular schedule MTA data (This data gets updated every 3 months-ish)
    response = requests.get(url)
    file = zipfile.ZipFile(io.BytesIO(response.content))
    stops_out = pd.read_csv(file.open("stops.txt"))[
        ["stop_id", "stop_name", "stop_lat", "stop_lon"]
    ]
    stops_out["stop_id"] = stops_out["stop_id"].astype(str)
    stop_times_out = pd.read_csv(file.open("stop_times.txt"))[
        ["trip_id", "stop_id", "arrival_time", "departure_time", "stop_sequence"]
    ]
    stop_times_out["stop_id"] = stop_times_out["stop_id"].astype(str)
    return stops_out, stop_times_out


def format_mta_stops_data(stops_in: pd.DataFrame) -> gpd.GeoDataFrame:
    stops_in["geometry"] = stops_in.apply(
        lambda x: Point(x["stop_lon"], x["stop_lat"]), axis=1
    )
    stops_in = gpd.GeoDataFrame(stops_in, geometry="geometry", crs="epsg:4326").to_crs(
        "epsg:2263"
    )
    stops_in["stop_id"] = stops_in["stop_id"].apply(str)
    return stops_in
