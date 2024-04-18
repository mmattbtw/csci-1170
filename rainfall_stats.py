MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    months = [0] * 12

    input_rainfall(months)

    print(f"Total rainfall: {sum(months):.2f}")
    print(f"Average rainfall: {sum(months) / len(months):.2f}")
    print(f"Highest rainfall: {MONTH_NAMES[months.index(max(months))]}")
    print(f"Lowest rainfall: {MONTH_NAMES[months.index(min(months))]}")
    

def input_rainfall(months):
    for month in months:
            month_name = MONTH_NAMES[months.index(month)]
            rainfall = int(input(f"Enter rainfall for {month_name}: "))
            months[months.index(month)] = rainfall

if __name__ == "__main__":
    main()