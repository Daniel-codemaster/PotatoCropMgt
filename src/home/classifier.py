import random

def get_fertilizer_recommendation():
    recommendations = [
        ("110-80-80", "Green manure, farmyard manure (4.5 t/ha)"),
        ("95-65-65", "Vermicompost, cow manure (5 t/ha)"),
        ("110-80-80", "Bone meal, seaweed extract (4.5 t/ha)"),
        ("85-55-55", "Green manure, farmyard manure (4.5 t/ha)"),
        ("95-65-65", "Compost, green manure (4 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("70-40-40", "Cow manure, green compost (6 t/ha)"),
        ("70-40-40", "Farmyard manure, compost (5.5 t/ha)"),
        ("100-70-70", "Bone meal, seaweed extract (4.5 t/ha)"),
        ("85-55-55", "Vermicompost, cow manure (5 t/ha)"),
        ("80-50-50", "Compost, poultry manure (5-7 t/ha)"),
        ("80-50-50", "Vermicompost, farmyard manure (4 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("70-40-40", "Mulch, biochar (5-6 t/ha)"),
        ("110-80-80", "Vermicompost, cow manure (5 t/ha)"),
        ("85-55-55", "Biochar, poultry manure (6 t/ha)"),
        ("65-35-35", "Cow manure, green compost (6 t/ha)"),
        ("90-60-60", "Compost, poultry manure (5-7 t/ha)"),
        ("100-70-70", "Vermicompost, cow manure (5 t/ha)"),
        ("80-50-50", "Bone meal, seaweed extract (4.5 t/ha)"),
    ]
    
    return random.choice(recommendations)

def get_irrigation_schedule():
    schedules = [
        "Daily",
        "Every two days",
        "Every three days",
        "Every four days",
        "Every five days",
        "Every six days",
        "Every week",
        "Every two weeks",
        "Every three weeks",
        "Every four weeks",
        "Every months"
    ]
    return random.choice(schedules)