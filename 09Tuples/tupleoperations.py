# initializing a tuple
drinks = ("tea", "coffee", "juice")
print(drinks)
print(type(drinks))

# initializing a tuple with a single element
soda = ("cola",)
print(type(soda))

# retrieving an element with square bracket notation
chai = drinks[0]
print(chai)

# using slicing to get a new tuple
result = drinks[:2]
print(result)

# using len() to determine the number of elements
qty = len(drinks)
print(qty)

# using a for loop with a tuple
for item in drinks:
    print(item)

# using a comparison operator with a tuple
result = (8, 5, 17, 500) < (8, 5, 23, 19)
print(result)

# multiple assignment with a tuple
results = [98, 17]
(total, count) = results
print(total)
print(count)

# using a tuple as a dictionary key
res = {("Smith", "Alice"):92, ("Jones", "Bob"):89}
print(res)

# using the sorted() method with a tuple
beverages = sorted(drinks)
print(beverages)






