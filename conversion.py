# we use int() function to change some other data type to int

num = input("Hello, enter a number: ")

print(num)
print(type(num))

# type conversion
new_num = int(num)
print(type(new_num))


# This will probably raise an error - exception
my_age = "twenty"
age = int(my_age)