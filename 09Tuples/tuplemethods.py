# initializing a tuple
drinks = ("tea", "coffee", "juice")
print(drinks)
print(type(drinks))

# intializing a tuple with one element
soda = ("cola",)
print(type(soda))

# accessing an element with square bracket notation
chai = drinks[0]
print(chai)

# taking a slice from the tuple
beverage = drinks[:2]
print(beverage)

# using len() to determine the number of elements
qty = len(drinks)
print(qty)

# using a for loop with a tuple
for item in drinks:
    print(item)

# using a comparison operator with two tuples
result = (8, 5, 17, 500) < (8, 5, 23, 19)
print(result)

# multiple assignment with a tuple
results = [98, 17]
(total, count) = results
print(total)
print(count)

# using a tuple as a key in a dictionary
res = {("Smith", "Alice"):92, ("Jones", "Bob"):89}
print(res)

# using the sorted() function with a tuple
beverages = sorted(drinks)
print(beverages)
