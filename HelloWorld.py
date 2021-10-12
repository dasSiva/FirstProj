print("Hello world")  # comment#

#  This is a sample addition


sum = 0
a = 10
b = 20
if a < b:
    sum = a+b
    print(sum)


# Types cast
x = str(3)
y = int(3.5)
z = float(3)


print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# cases
a = "Siva"
A = "Das"
print(a)
print(A)


# Illegal var name

myvar = "Das"
my var = "Das"  # illegal
print(myvar)
print(my var)  # error case

# practise program
a = 2
b = 3
if a < b:
    sum = a+b
    print(sum)

# typecasting to float
a = 2
b = float(a)
print(b)

x = "Siva"
y = "das"
z = x+y
print(z)

x = 2
y = 3
z = x+y
print(z)

x = "awesome"


def myfunc():
    print("Python is" + x)


myfunc()


xyz = "Global"


def myfund():
    xyz = "function"
    print(xyz)


myfund()
print(xyz)

# convert float to int
x = 2.3
a = int(x)
print(a)

a = "Hello, World!"
print(a[-2])


for everyElement in "Banana":
    print(everyElement)


a = "hello!"
print(len(a))

txt = "best things in life are free!"
print("best" in txt)

# Escaped used for " , ' and \
cleartxt = "Aca\',\"&\\"

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"

secret = "".join([abc[(abc.find(c)+3) % 71] for c in cleartxt])

print(secret)


# escape
txt = "we are the \"humans\" "
print(txt)


# String methods
txt = "hello world"
print(txt.capitalize())

txt = "Hello world"
print(txt.casefold())

txt = "Hello åßrld"
x = txt.encode()
print(x)

txt = "Hello"

print(txt.isprintable())`


a = ",,,,,...... apple"
print(a.lstrip(",."))

a = "Hello Sam!"
x = a.maketrans("S", "P")
print(a.translate(x))

a = "I like apples"
print(a.replace("apples", "bananas"))
