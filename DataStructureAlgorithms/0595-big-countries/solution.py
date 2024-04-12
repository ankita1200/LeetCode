import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big = (world["area"] >= 3000000) | (world["population"] >= 25000000)
    countries = world[big][["name","population","area"]]
    return countries
