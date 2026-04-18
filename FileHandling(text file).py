# file handling-text file
# 1.write the file
file = open("sample.txt", "w")
file.write("hello my name is Diya")
file.close

# 2.read the file
file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()

# 3.append the file
file = open("sample.txt", "a")
file.write("\nwelcome to python")s
file.close()
