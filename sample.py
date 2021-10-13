

xx = input("enter a number")
Mynum = int(xx)
yy = 10
if yy < Mynum:
    print("entered number is higher")

elif yy > Mynum:
    print("entered number is lesser")

else:
    print("entered number is equal")


# multiple line
    a = ("""this is a long string,
     written with the intention to print it,
      in multiple lines""")
    print(a)


# string arrays
    a = ("hello")
    print(a[2])

# loop through a string
for everyelement in "Apples":
    print(everyelement)


#   length of string
a = "universe"
print(len(a))

# check string

a = "it's sunny outside"
print("sunny" in a)


a = "it's sunny outside"
if "sunny" in a:
    print("yes, sunny is present")

#  not statement
a = "it's sunny outside"
print("not" not in a)


# using if not statement
a = "it's sunny outside"
if "not" not in a:
    print("'not', is not present")

    # slicing
    a = "planet earth"
    print(a[1:5])

    a = "planet earth"
    print(a[:5])

    a = "planet earth"
    print(a[0:])

 a= "planet earth"
 print(a[-3:-1])

# Uppercase
 a="sealife"
 print(a.upper())

# lowercase/
 a=SEALIFE
 print(a.lower())

# strip
a="sign board  "
print(a.strip())


# replace string
a= "earth"
print(a.replace("e","a"))

# split
a= "hello, world"
print(a.split(","))



a= "Haritha Hari" 
c= "Haritha"
b= a[7:]
print(c+(b.replace("Hari", "Sivadas")))

# add space

a= "hello"
b= "world"
print(a+ " " +b)

# format
age = 36
txt= ("my name is john and my age is {}")
print(txt.format(age))

# function
def formatfn():
    quantity=input("enter qnty")
    itemno= input("enter itemno")
    price = input("enter price")
    myorder = "I want {} quantity of itemno {} for {} dollars"
    print(myorder.format(quantity,itemno,price))

formatfn()    




x=10
x=x+1
x+=1
if x==0:
    print("")

bool("abc"=="cft")
print(bool(15))



x=10
x+=20
print(x)
# x+=20 is the same as below
x=10
z=x
y=x+20
x=y

# swap the values
aq="hari"
bq="siva"
c= bq
d= aq

print(aq)
print(bq)



