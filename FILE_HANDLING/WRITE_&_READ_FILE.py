# Writing
file = open("demo.txt", "w")
file.write("Hello Python\n")
file.write("This is file handling example.")
file.close()

# Reading
file = open("demo.txt", "r")
print(file.read())
file.close()