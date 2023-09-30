import re
input_string = input("Enter a string: ")
if re.search("^[a-zA-Z0-9]+$", input_string):
 print("The string contains only allowed characters.")
else:
 print("The string contains disallowed characters.") 