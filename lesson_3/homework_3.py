import copy
from random import randint

# Task 1:
# Task 1.1:
Regular_list = [1, 2, 3, 4, 5]                      # Create a list
print('Task 1.1:', Regular_list)

# Task 1.2:
List_constructor = [x**2 for x in [1,2,3,4]]        # Create a list using list constructor
print('Task 1.2:', List_constructor)

# Task 1.3.1:
text = "Python is a whole world!!!"
List_string = list(text)                            # Create a list of strings
print('Task 1.3.1:', List_string)

# Task 1.3.2:
print('Task 1.3.2:', text.split( ))                 # Create a list using the split method

# Task 1.4:
List_for = [str(x) for x in text]                   # Create list using list comprehension
print('Task 1.4:', List_for)

# Task 2:
# Task 2.1:
Regular_list.append(6)                              # Add item to the end of the Regular_list
print('Task 2.1:', Regular_list)

# Task 2.2:
List_constructor.insert(1, 99)                      # Add item to List_constructor at fixed index
print('Task 2.2:', List_constructor)

# Task 2.3:
del Regular_list[-1]                                 # Remove item from Regular_list at fixed index
print('Task 2.3:', Regular_list[-1])

# Task 2.4:
Regular_list.remove(3)                              # The function removes a specific Regular_list item.
print('Task 2.4:', Regular_list[3])

# Task 2.5:
List_constructor.pop(0)                             # The function 'pop' deletes a list item by its index
print('Task 2.5:', List_constructor)

#Task 3:
# Task 3.1:
apple = [21, 10, 18, 5, 15, 4, 2, 1, 30]
apple.sort()                                        # sorting by increment list using function 'sort'
plum = [21, 10, 18, 5, 15, 4, 2, 1, 30]
plum.reverse()                                     # sorting the list in descending order using the function 'reverse'

print('Task 3.1:', apple, plum, sep='\n')

# Task 3.2: Ascending sorting algorithm
# create a list
n = 10                                             # list length
pear = []
for i in range(n):
    pear.append(randint(1, 99))                    # use a random number generator
print('Task 3.2: Unordered list',pear)

def sort_function(c):
    for j in range(0,c - 1):                           # outer loop counts the number of "passes" in the list
        for a in range(0,c - j -1):                     # nested cycle compares i-th and i + 1-th element and,
                                                     # if necessary, changes their places the number of
                                                     # comparisons each time decreases by j
            if pear[a] > pear[a+1]:
                pear[a],pear[a + 1] = pear[a + 1], pear[a]
print('Task 3.2: Sorted list', pear)

# Task 4:
# Task 4.1:
The_sun = [-1, 2, 0, 10, 3, 4, -5, -10, 8, 1, 3, -2, 12, -4, -8, 9]     # list with numbers not ordered
Mercury = list (filter(lambda x : x > 0, The_sun))                      # Filter numbers > 0 using Filter function
                                                                        # with lambda
print("Task 4.1:", Mercury)

# Task 4.2:
Venus = list (filter(lambda x: isinstance(x, int) and x > 0, The_sun))  # Filter numbers > 0 using Filter function
                                                                        # with callback
print("Task 4.2:",Venus)

# Task 4.3:
Earth = [x for x in The_sun if x > 0]                                   # Filter number > 0 using list comprehension.
print("Task 4.3:", Earth)

# Task 4.4:
The_sun2 = The_sun                                                      # Create copy of link for this list.
print("Task 4.4:", The_sun2)

# Task 4.5:
The_sun3 = copy.deepcopy(The_sun)                                       # Create copy of list using module copy.deepcopy
print("Task 4.5:", The_sun3)

# Task 4.6:
The_sun4 = The_sun.copy()                                               # Create copy of list using list slices.
print("Task 4.6:", The_sun4)

# Task 4.7:
Mars = [x * 5 for x in The_sun]                                         # Multiply all elements of the The_sun list by 5
print("Task 4.7:", Mars)

# Task 4.8:
Jupiter = ','.join(map(str, The_sun))                                   # Combine all elements of the list into a string
print("Task 4.8:", Jupiter)

# Task 4.9:
# for item in The_sun:print ("Task 4.9:",item)

# Task 4.11:
Saturn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Titanium = [i*2 for i in Saturn]                  # Change every list item

print("Task 4.11:", Titanium)

# Task 4.12:
Ray = list(map(lambda x: x * 3, Saturn))    # Change each element of the list using the lambda function
print("Task 4.12:", Ray)

# Task 4.13:
Uranus = [10, 15, 20, 5, 0, -20, -5, -10, 25]
Titania = min(Uranus)                             # Find the minimum value of the list using the standard function
print("Task 4.13:", Titania)

# Task 4.14:
Oberon = max(Uranus)                               # Find the maximum value of the list using the standard function
print("Task 4.14:", Oberon)

# Task 4.15 - 4.16:
Neptune = [10, 15, 20, 5, 0, -20, -5, -10, 25]
def minmax1 (x):
    minimum = maximum = x[0]
    for b in x[1:]:
        if b < minimum:
            minimum = b
        else:
            if b > maximum: maximum = b
    return minimum, maximum
print("Task 4.15 - 4.16:",minmax1(Neptune))



# region comments for homework 3 tasks 1-3
# TODO: common issue - You should numerate each sub task with some comment
# TODO: common issue - You should wrap blocks of functional code into regions. It will allow you to expand and
#                      collapse it into lists.
# TODO: common issue - Hard to understand all this prints. Please add description for each print. For example "Not
#                      sorted list", "Sorted list"
# TODO: common issue - before next push try to sue code analyzer > Code -> Inspect Code -> Whole project -> OK.
#                      Remove all warnings issues and errors from iteration to iteration until no errors left.
# TODO: line 4 - make space after comma
# TODO: line 7 - customization of str to str make no sense
# TODO: line 9 - best practice to use one code style. In python no difference between such two strings 'Python' and
#                "Python". Try to use single quotes for internal strings or for separated characters ("my outer
#                string 'my inner string'", "Simple string", '\n', 'n').
# TODO: lines 16-17 - please write difference between both methods. Try to print result of this functions to see
#                     difference.
# TODO: line 19 - you print almost same lists as in task 1. Please create 1 set of variables for work but with noto
#                 so confusing names.
# TODO: line 21 - no space after # before comment text
# TODO: line 30 - 2 emtpy lines should be before function declaration.
# TODO: line 33 - all variables and attributes should be lower case with underscore
# TODO: line 36 - all variables and attributes should be lower case with underscore
# TODO: line 31 - why do you create another one internal variable of array if you can use array from arguments?
# TODO: line 31 - variable name is confusing and not clear destination of such variable
# TODO: line 32 - variable name is confusing and not clear destination of such variable
# TODO: line 34 - variable name is confusing and not clear destination of such variable
# TODO: line 37 - variable name is confusing and not clear destination of such variable
# TODO: lines 31 - 40 - no comments. Please add some comments about work of your algorithm.
# TODO: line 42 - no empty line after code
# endregion
