file_name = input("Enter the file name: ")
file = open(file_name, "r")

line = file.readline().strip()
line_num = 1

while line != "":
    print(line_num, line)
    line_num += 1
    line = file.readline().strip()

file.close()