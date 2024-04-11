file_name = input("Enter file name: ")
file = open(file_name, "r")

line = file.readline().strip()
line_number = 1

while line_number <= 5 and line != "":
    print(line)
    line_number += 1
    line = file.readline().strip()

file.close()