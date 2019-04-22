import re # regex package for python
def groceries(text):
    regex = re.compile(r'\d+\s\w+') # compile the regex pattern that you want to find
    return regex.findall(text) # return all matches of the compiled pattern

print(groceries('12 carrots, 3 mushrooms, 4 eggs, 5 lettuce, 10 cabbage'))
