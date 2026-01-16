import pandas as pd
ex = pd.read_csv('exercises.csv')
nu = pd.read_csv('nutrition.csv')
print(f"Exercises: {len(ex)}")
print(f"Nutrition: {len(nu)}")
assert len(ex) >= 1000
assert len(nu) >= 1000
print("Verification Success!")
