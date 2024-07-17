#1. Creating an empty list:
#To create an empty list in Python, you can use:
empty_list = []
#2. Accessing the third element in a list:
#If 'my_list' is your list, you can access the third element (index 2) using:
my_list = []
third_element = my_list[2]
#3. Adding an element 'apple' to the end of a list named fruits:
#You can add 'apple' to the end of the `fruits` list using the `append()` method:
fruits = []
fruits.append('apple')
#4. Removing the third element from a list named numbers:
# To remove the third element (index 2) from 'numbers' , you can use 'pop()':
numbers = []
numbers.pop(2)
#5. Difference between 'append()' and 'extend()' methods:
#'append()' adds its argument as a single element to the end of a list.
#'extend()' iterates over its argument adding each element to the list, extending the list.
#6. Checking if 'banana' exists in a list named fruits:**
#To check if 'banana' exists in `fruits`, you can use the `in` keyword:
fruits = []
if 'banana' in fruits : print("Yes, 'banana' is in the list.")
#7. Output of `len(['a', 'b', 'c'])`:
#The output will be:3
#8. Reversing the order of elements in a list named my_list:
#You can reverse `my_list` using slicing:
reversed_list = my_list[::-1]
#9. Purpose of the `sort()` method in Python lists:
#The `sort()` method sorts the elements of a list in place, i.e., it modifies the original list to be in ascending order.
#10.
#11. String in Python:
#A string in Python is a sequence of characters enclosed within quotes (single `'` or double `"`).
#12. Creating an empty string:**
#You can create an empty string by assigning an empty pair of quotes:
empty_string = ""
#13. Accessing characters in a string using indexing:
#Yes, you can access characters in a string using square brackets and an index:
my_string = ""
char = my_string['index']
#14. Finding the length of a string:**
#You can find the length of a string using the `len()` function:
length = len(my_string)
#15. Concatenating two strings:
#Strings can be concatenated using the `+` operator:
#concatenated_string = string1 + string2
string_1 = ()
string_2 = ()
print(string_1 + string_2 )
#16. Converting a string to uppercase:
#Use the `upper()` method:
#uppercase_string = my_string.upper()
print(my_string.upper)
#17. Converting a string to lowercase:
#Use the `lower()` method:
#lowercase_string = my_string.lower()
print(my_string.lower)
#18. Checking if a substring exists in a string:
#Use the `in` keyword:
if 'substring' in my_string:print("Substring found.")
#19. Making a string into a list of substrings:
#Use the `split()` method:
substrings_list = my_string.split()
#20. Replacing occurrences of a substring within a string:
#Use the `replace()` method:
new_string = my_string.replace('old_substring', 'new_substring')
#21. Finding the index of a substring within a string:
#Use the `find()` method or `index()` method:
index = my_string.find('substring')
#22. Iterating over the characters of a string:
#You can iterate over characters in a string using a for loop:
for char in my_string:
  print(char)
#23. Reversing a string in Python:
#You can reverse a string using slicing:
reversed_string = my_string[::-1]
#24. Converting an integer or float to a string:
#Use the `str()` function:
number = ()
num_str = str(number)
#25. Checking if a string contains only digits:
#Use the `isdigit()` method:
if my_string.isdigit():print("String contains only digits.")
#26. Finding the sum of all elements in a list of numbers:
#You can use the `sum()` function:
total_sum = sum(numbers_list)
#27. Accessing the third element of a list:
#Use indexing:
third_element = my_list[2]
#28. Finding the maximum and minimum elements in a list of numbers:
#Use the `max()` and `min()` functions:
max_element = max(numbers_list)
min_element = min(numbers_list)
#29. List comprehension in Python:
#List comprehension provides a concise way to create lists:
squares = [x**2 for x in range(10)]
#30. Checking if a specific element exists in a list:**
#Use the `in` keyword:
if element in my_list:print("Element found.")
#31. Reversing a list:
#You can reverse a list using slicing: