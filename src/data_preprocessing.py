import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Check missing values
    df = df.dropna()

    return df
