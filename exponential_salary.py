salary = 1
days = int(input("Number of days "))

for i in range(0, days):
    print(f"Day {i+1:<10} {salary/100:<10}")
    salary *= 2