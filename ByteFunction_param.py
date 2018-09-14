#Thew names given in the function definition are called parameters
#values you supply in the functions call are called arguments
#def print_max is a function with two arguments a and b
def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to ", b)
    else:
        print(b, "is maximum")

#directly pass literal values
print_max(3, 4)

x = 5
y = 7

#pass variables as arguments
print_max(x, y)

#we have the function twice, each with different values as a and b
#let's call the function a third time
print_max(9, 2)