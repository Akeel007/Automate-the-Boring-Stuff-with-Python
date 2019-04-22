import re
def groceries(text):
    regex = re.compile(r'\d+\s\w+')
    return regex.findall(text)

print(groceries('12 carrots, 3 mushrooms, 4 eggs, 5 lettuce, 10 cabbage'))
