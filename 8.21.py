#Variables
import array as arr

a = 10
b = 10.00
c = "Hello World"
d = True
e = {1, 2, 3, 4, 5}
f = ["apple", "banana", "cherry", 1, 2, 3, 4, 5]
g = ("apple", "banana", "cherry", 1, 2, 3, 4, 5)
h = arr.array('i', [1, 2, 3, 4, 5])

i = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, a, c, a, "Hello-World", b]

j = set(i)

print(i)
print(j)


#Data Types

print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
print(f"Type of c: {type(c)}")
print(f"Type of d: {type(d)}")
print(f"Type of e: {type(e)}")
print(f"Type of f: {type(f)}")
print(f"Type of g: {type(g)}")
print(f"Type of h: {type(h)}")
def add(x, y):
    print("This line will get executed")
    return x + y
    print("This line will never be executed")

x = add(10,5)

print(x)

