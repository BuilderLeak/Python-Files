file = str(input("Enter file name: "))
file = open("my_file.txt", "x")
file.write("Hello Gitam CSE!")
file.close()

file = open("my_file.txt", "r")
print(file.read())