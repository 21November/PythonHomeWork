word = "Hello"

letter_H_1 = word[0] # prints the letter with the 0th index
letter_E_1 = word[1] # prints the letter with the 1th index
letter_L_1 = word[2] # prints the letter with the 2th index
letter_L_2 = word[3] # prints the letter with the 3th index
letter_O_1 = word[4] # prints the letter with the 4th index
every_second_letter = word[::2] # output of every second character of a word
reverse_word = word[::-1] # character word output in reverse order

print(letter_H_1, letter_E_1, letter_L_1, letter_L_2, letter_O_1, every_second_letter, reverse_word, sep='\n\n\n')

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