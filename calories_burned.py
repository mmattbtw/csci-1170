calories = 4.2
minutes = 10
print("Minutes, Calories Burned", "------------------------", sep="\n")
while minutes <= 30:
    calories_burned = calories * minutes
    print(f"{minutes:<10}{calories_burned:>10.1f}")
    minutes += 5