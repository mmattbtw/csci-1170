total = 0
ns = [10,25,100]
for n in ns:
    for num in range(1, n+1):
        total+=1/num
    print(f"When n={n}, y={total}")