def calculate_risk_score(screen_time, night_usage, app_usage, day_usage):
    # Simple risk calculation based on usage
    risk_score = (screen_time * 0.3 + app_usage * 0.2 + night_usage * 0.3 + day_usage * 0.2)
    
    if risk_score > 10:
        risk_level = 'High Risk'
    elif risk_score > 5:
        risk_level = 'Moderate Risk'
    else:
        risk_level = 'Low Risk'
    
    return risk_score, risk_level