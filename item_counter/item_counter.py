def main():
    file = open("names.txt", "r")
    name = file.readline()
    count = 0
    while name != "":
        count += 1
        name = file.readline()
    file.close()
    print(f"There are {count} names.")

if __name__ == "__main__":
    main()