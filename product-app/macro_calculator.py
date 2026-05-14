def calculate_macros(food_items, sample_data):
    macros = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    
    for item in food_items:
        food_name = item["name"]
        quantity = item["quantity"]
        
        if food_name in sample_data:
            food_macros = sample_data[food_name]
            macros["calories"] += food_macros["calories"] * quantity
            macros["protein"] += food_macros["protein"] * quantity
            macros["carbs"] += food_macros["carbs"] * quantity
            macros["fats"] += food_macros["fats"] * quantity
    
    return macros