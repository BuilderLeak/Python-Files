new_list = []
my_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
for index, value in enumerate(my_list):
    if index not in [0, 4, 5]:
        new_list.append(value)
print(new_list)