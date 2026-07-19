import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_data():
    forest_fires = fetch_ucirepo(id=162)

    X = forest_fires.data.features
    y = forest_fires.data.targets

    df = pd.concat([X, y], axis=1)

    return df