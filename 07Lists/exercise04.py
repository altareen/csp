romeo = "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"

words = romeo.split()
print(words)

# remove the duplicates from the list
result = []
for item in words:
    if item not in result:
        result.append(item)
print(result)

# sort the list in alphabetical order
result.sort()
print(result)


