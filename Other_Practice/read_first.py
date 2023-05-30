with open('read.csv', 'r') as file:
    read = file.readline()
    print(read)

if read:
    print("First line is not none")
else:
    print("First Line is  blank")