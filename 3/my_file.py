file = open("my_file.txt", "a")
file.write("Hello Gitam CSE!")
file.close()

file = open("my_file.txt", "r")
print(file.read())