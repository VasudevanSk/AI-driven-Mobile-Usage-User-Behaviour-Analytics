from sklearn.cluster import KMeans
import pandas as pd

def apply_clustering(df):
    # Select numeric columns for clustering
    numeric_cols = df.select_dtypes(include=[float, int]).columns
    X = df[numeric_cols]
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    return df, kmeans
