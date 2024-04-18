def main():
    file = open("steps.txt")
    steps = []
    for line in file:
        steps.append(int(line.strip()))

    print("Median:", Median(steps), "Mean:", Mean(steps), "Mode:", Mode(steps))

    file.close()

def Median(steps):
    numbers = steps[:]
    numbers.sort()
    
    if len(numbers) % 2 == 0:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2

def Mean(steps):
    return sum(steps) / len(steps)

def Mode(steps):
    max_count = 0
    mode = 0
    for number in steps:
        if steps.count(number) > max_count:
            max_count = steps.count(number)
            mode = number
    
    return mode

if __name__ == "__main__":
    main()