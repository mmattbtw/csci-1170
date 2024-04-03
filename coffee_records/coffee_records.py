import os


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

def update_records():
    original_file = open("records.txt", "r")
    temp_file = open("temp.txt", "w")
    search = input("What brand would you like to update? ")
    found = False
    for line in original_file:
        if line.strip() == search:
            quantity = original_file.readline()
            print(f"Current quantity: {quantity.strip()}")
            new_quantity = input("What is the new quantity? ")
            temp_file.write(f"{line.strip()}\n{new_quantity}\n")
            found = True
        else:
            quantity = original_file.readline()
            temp_file.write(f"{line.strip()}\n{quantity.strip()}\n")
    if found == False:
        print("Brand not found.")
    original_file.close()
    temp_file.close()
    os.remove("records.txt")
    os.rename("temp.txt", "records.txt")

def main():
    choice = input("What would you like to do? (add/read/search/update) ")
    if choice == "add":
        add_record()
    elif choice == "read":
        read_records()
    elif choice == "search":
        search_records()
    elif choice == "update":
        update_records()

if __name__ == "__main__":
    main()