import random
def RollingDice():
    return random.randint(1,6) + random.randint(1,6)

def main():
    sum7 = 0
    sum5 = 0
    sum6 = 0
    sum12 = 0
    for i in range(0,100000):
        num = RollingDice()
        if num == 7:
            sum7 += 1
        elif num == 5:
            sum5 += 1
        elif num == 6:
            sum6 += 1
        elif num == 12:
            sum12 += 1
    print("7", sum7, "5", sum5, "6", sum6, "12", sum12)

if __name__ == "__main__":
    main()
