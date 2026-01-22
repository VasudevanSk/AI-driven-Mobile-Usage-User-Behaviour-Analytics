from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

def train_classifier(df):
    encoder = LabelEncoder()
    df['label'] = encoder.fit_transform(df['cluster'])

    X = df[['screen_time', 'app_usage', 'night_usage', 'day_usage']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, encoder, accuracy
