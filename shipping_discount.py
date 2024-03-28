quantity = int(input("Number of packages "))

price = 99

if quantity >= 100:
    discount = .5
elif quantity >= 50:
    discount = .4
elif quantity >= 20:
    discount = .3
elif quantity >= 10:
    discount = .2
else:
    discount = 0

final_price = price*quantity - ((price*quantity)*discount)
print(f"Price: {final_price:.2f}")