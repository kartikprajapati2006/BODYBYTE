import pandas as pd
import numpy as np

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    category = ""
    if bmi < 18.5: category = "Underweight"
    elif 18.5 <= bmi < 25: category = "Normal"
    elif 25 <= bmi < 30: category = "Overweight"
    else: category = "Obese"
    return round(bmi, 2), category

def calculate_tdee(weight, height, age, gender, activity_level):
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    multipliers = {
        'Sedentary': 1.2,
        'Lightly Active': 1.375,
        'Moderately Active': 1.55,
        'Very Active': 1.725,
        'Extra Active': 1.9
    }
    tdee = bmr * multipliers.get(activity_level, 1.2)
    return round(tdee)

# Test Cases
print("Testing BMI Logic...")
bmi, cat = calculate_bmi(70, 175)
print(f"BMI: {bmi}, Category: {cat}")
assert bmi == 22.86
assert cat == "Normal"

print("\nTesting TDEE Logic...")
tdee = calculate_tdee(70, 175, 25, 'Male', 'Moderately Active')
print(f"TDEE: {tdee}")
assert tdee > 2000

print("\nTesting Dataset Loading...")
ex_df = pd.read_csv('exercises.csv')
nu_df = pd.read_csv('nutrition.csv')
print(f"Exercises: {len(ex_df)}, Nutrition: {len(nu_df)}")
assert not ex_df.empty
assert not nu_df.empty

print("\nAll tests passed!")
