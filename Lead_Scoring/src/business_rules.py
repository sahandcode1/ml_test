def apply_business_rules(data, prediction):
    score = prediction
    
    if data["region"] == 'Tehran' and data["total_purchases"] > 0: 
        score = 1

    if data['last_interaction_days'] > 100:
        score = 0

    return score