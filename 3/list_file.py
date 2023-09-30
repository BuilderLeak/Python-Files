my_list = ['apple', 'banana', 'cherry']
list_string = '\n'.join(my_list)

file = open('list_output.txt', 'w')
file.write(list_string)
file.close()