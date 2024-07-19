# we will work on an example about immutable data type
x = 5
y = x


print("x: ", x)
print("y: ", y)

# assign another value for x
x = 29
print("x:", x)
print("y:", y)


print("---" * 5)

# Working with a mutable data type - list
a = [2, 4, 6]

b = a

print("a list:", a)
print("b list: ",b )

b[0] = 99
print("b list after changing the first element: ", b)
print("Checking the list stored in a: ", a)
