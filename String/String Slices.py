line = "Hello Python"

line_characters = '\n''\n''\n'.join(line) # output each character individually
every_second_letter = '\n''\n''\n'.join(line[::2]) # output of every second character of a line
return_line = '\n''\n''\n'.join(line[::-1]) # character string output in reverse order

print(line_characters,'\n''\n''\n', every_second_letter, '\n''\n''\n', return_line)
