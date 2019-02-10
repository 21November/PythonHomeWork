line = "Hello"

line_characters = '\n''\n''\n'.join(line)            # output each character individually
every_second_letter = '\n''\n''\n'.join(line[::2])   # output of every second character of a line
return_line = '\n''\n''\n'.join(line[::-1])          # character string output in reverse order

print(line_characters,'\n''\n''\n', every_second_letter, '\n''\n''\n', return_line)

# region comments for code review iteration #1
# line 1: Name of string variable is confusing.
#         Which line do you mean?
# line 3: Please don't use '\n' in variable it is hard to read such variable.
#         Please create separate variable for each letter
#         Name of variable is confusing. Characters of which line do you mean?
# line 4: Please don't use '\n' in variable
#         Please just use slice of string it will return needed characters into the new string.
# line 5: Name of variable is confusing.
#         Please use reversed string name instead of current name.
#         Please don't use '\n' character in variable.
# line 7: Please don't use '\n' character as values.
#         Please take a look on documentation for print function (sep argument)
# endregion
