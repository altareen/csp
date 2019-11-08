romeo = "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"

words = romeo.split()
print(words)

result = []
for item in words:
    if item not in result:
        result.append(item)
print(result)
result.sort()
print(result)




