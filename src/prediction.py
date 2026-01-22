def predict_user(model, encoder, new_user):
    cluster = model.predict([new_user])[0]
    label = encoder.inverse_transform([cluster])[0]
    if label == 0:
        recommendation = "Continue healthy habits"
    elif label == 1:
        recommendation = "Reduce screen time at night"
    else:
        recommendation = "Maintain balance"
    return label, recommendation
