menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)


# a = [[96], [69]]

# x = ''.join(list(map(str, a)))
# print(list(map(str, a)))
# print(type(x))
# print(x)