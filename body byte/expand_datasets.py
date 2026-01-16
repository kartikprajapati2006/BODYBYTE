import pandas as pd
import random

# Mapping of body parts/exercises to high-quality specific Unsplash images
image_mapping = {
    "back": "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&q=80&w=600",
    "legs": "https://images.unsplash.com/photo-1574680096145-d05b474e2158?auto=format&fit=crop&q=80&w=600",
    "chest": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&q=80&w=600",
    "arms": "https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&q=80&w=600",
    "shoulders": "https://images.unsplash.com/photo-1541534741688-6078c64b52d2?auto=format&fit=crop&q=80&w=600",
    "abs": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&q=80&w=600",
    "full body": "https://images.unsplash.com/photo-1599058917212-d750089bc07e?auto=format&fit=crop&q=80&w=600",
    "default": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=600"
}

# --- Exercise Dataset Generation ---
exercises_base = [
    {"Name": "Pull Up", "Part": "back", "Muscle": "lats", "Eq": "body weight", "Lvl": "Intermediate", "Goal": "Fitness"},
    {"Name": "Squat", "Part": "legs", "Muscle": "quads", "Eq": "barbell", "Lvl": "Beginner", "Goal": "Muscle Gain"},
    {"Name": "Push Up", "Part": "chest", "Muscle": "pecs", "Eq": "body weight", "Lvl": "Beginner", "Goal": "Fitness"},
    {"Name": "Deadlift", "Part": "back", "Muscle": "hamstrings", "Eq": "barbell", "Lvl": "Advanced", "Goal": "Muscle Gain"},
    {"Name": "Plank", "Part": "abs", "Muscle": "core", "Eq": "body weight", "Lvl": "Beginner", "Goal": "Weight Loss"},
    {"Name": "Bicep Curl", "Part": "arms", "Muscle": "biceps", "Eq": "dumbbell", "Lvl": "Beginner", "Goal": "Muscle Gain"},
    {"Name": "Shoulder Press", "Part": "shoulders", "Muscle": "delts", "Eq": "dumbbell", "Lvl": "Intermediate", "Goal": "Fitness"},
    {"Name": "Lunges", "Part": "legs", "Muscle": "glutes", "Eq": "body weight", "Lvl": "Beginner", "Goal": "Fitness"},
    {"Name": "Burpees", "Part": "full body", "Muscle": "cardio", "Eq": "body weight", "Lvl": "Intermediate", "Goal": "Weight Loss"},
    {"Name": "Mountain Climbers", "Part": "abs", "Muscle": "core", "Eq": "body weight", "Lvl": "Intermediate", "Goal": "Weight Loss"}
]

exercise_data = []
for i in range(1100):
    base = random.choice(exercises_base)
    goal_choice = random.choice(["Muscle Gain", "Weight Loss", "Fitness", "Body Building"])
    lvl_choice = random.choice(["Beginner", "Intermediate", "Advanced"])
    
    # Select image based on body part
    img_url = image_mapping.get(base['Part'], image_mapping['default'])
    
    exercise_data.append({
        "Exercise_Name": f"{base['Name']} Var-{i}",
        "BodyPart": base['Part'],
        "Target_Muscle": base['Muscle'],
        "Equipment": base['Eq'],
        "Level": lvl_choice,
        "Goal": goal_choice,
        "Image_URL": img_url,
        "Instructions": f"Perform {base['Name']} variation number {i}. Ensure proper form and controlled breathing."
    })

ex_df = pd.DataFrame(exercise_data)
ex_df.to_csv('exercises.csv', index=False)
print(f"Generated {len(ex_df)} exercises with mapped images.")

# (Nutrition generation remains unchanged but re-run for consistency)
foods_base = [
    {"Item": "Oatmeal", "Cat": "Breakfast", "Cal": 300, "P": 10, "C": 50, "F": 5, "Goal": "Weight Loss"},
    {"Item": "Eggs", "Cat": "Breakfast", "Cal": 250, "P": 18, "C": 2, "F": 15, "Goal": "Muscle Gain"},
    {"Item": "Chicken Breast", "Cat": "Lunch", "Cal": 400, "P": 45, "C": 0, "F": 10, "Goal": "Muscle Gain"},
    {"Item": "Salad", "Cat": "Lunch", "Cal": 200, "P": 5, "C": 20, "F": 10, "Goal": "Weight Loss"},
    {"Item": "Salmon", "Cat": "Dinner", "Cal": 500, "P": 35, "C": 0, "F": 30, "Goal": "Fitness"},
    {"Item": "Steak", "Cat": "Dinner", "Cal": 700, "P": 50, "C": 0, "F": 40, "Goal": "Muscle Gain"},
    {"Item": "Protein Shake", "Cat": "Snack", "Cal": 150, "P": 25, "C": 5, "F": 2, "Goal": "Muscle Gain"},
    {"Item": "Greek Yogurt", "Cat": "Snack", "Cal": 180, "P": 15, "C": 12, "F": 3, "Goal": "Fitness"},
    {"Item": "Almonds", "Cat": "Snack", "Cal": 160, "P": 6, "C": 6, "F": 14, "Goal": "Weight Loss"},
    {"Item": "Quinoa Bowl", "Cat": "Lunch", "Cal": 450, "P": 15, "C": 70, "F": 10, "Goal": "Fitness"}
]

nutrition_data = []
for i in range(1100):
    base = random.choice(foods_base)
    goal_choice = random.choice(["Muscle Gain", "Weight Loss", "Fitness", "Body Building"])
    nutrition_data.append({
        "Food_Item": f"{base['Item']} Type-{i}",
        "Category": base['Cat'],
        "Calories": base['Cal'] + random.randint(-50, 50),
        "Protein": max(2, base['P'] + random.randint(-5, 5)),
        "Carbs": max(0, base['C'] + random.randint(-10, 10)),
        "Fat": max(0, base['F'] + random.randint(-5, 5)),
        "Goal_Alignment": goal_choice
    })

nu_df = pd.DataFrame(nutrition_data)
nu_df.to_csv('nutrition.csv', index=False)
print(f"Generated {len(nu_df)} food items.")
