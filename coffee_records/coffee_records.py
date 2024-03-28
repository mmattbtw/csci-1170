def add_record():
    continue_adding = True
    file = open("records.txt", "a")
    while continue_adding == True:
        brand_name = input("Input brand name: ")
        quantity = input("Input quantity: ")
        file.write(f"{brand_name}\n{quantity}\n")
        continue_adding = input("Would you like to add another record? (y/n) ") == "y"
    file.close()

def read_records():
    file = open("records.txt", "r")
    brand_name = file.readline()
    quantity = file.readline()
    while brand_name != "":
        print(f"Brand: {brand_name.strip()}")
        print(f"Quantity: {quantity.strip()}")
        brand_name = file.readline()
        quantity = file.readline()
    file.close()

def search_records():
    file = open("records.txt", "r")
    search = input("What brand are you looking for? ")
    found = False
    for line in file:
        if line.strip() == search:
            print(f"Brand: {line.strip()}")
            quantity = file.readline()
            print(f"Quantity: {quantity.strip()}")
            found = True
    if found == False:
        print("Brand not found.")
    file.close()

def main():
    choice = input("What would you like to do? (add/read/search) ")
    if choice == "add":
        add_record()
    elif choice == "read":
        read_records()
    elif choice == "search":
        search_records()

if __name__ == "__main__":
    main()