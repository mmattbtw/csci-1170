weight = float(input("asdf "))
if weight >= 10:
    cost = 3.80
elif weight >= 6:
    cost = 3.70
elif weight >= 2:
    cost = 2.20
else:
    cost = 1.10

print (f"Shipping cost: {weight/cost:.2f}")