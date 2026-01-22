import sys
sys.path.append('src')
from prediction import predict_user
from classification_model import train_classifier
from clustering_model import apply_clustering
from data_preprocessing import load_and_clean_data

df = load_and_clean_data('data/mobile_usage.csv')
df, _ = apply_clustering(df)
model, encoder, accuracy = train_classifier(df)

print('Calling predict_user')
try:
    result = predict_user(model, encoder, [5.0, 40, 3.0, 2.0])
    print('Result:', result)
except Exception as e:
    print('Error:', e)
