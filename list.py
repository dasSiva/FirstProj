
# list
thislist = ["apple", "banana", "cherry"]
intlist = [1, 2, 3, 4]
fltlist = [1.2, 3.4, 2.3]
print(len(thislist[1]))

print(intlist)
print(fltlist)

print(type(intlist))

# replace item in list/


class zoo():
    def animals():
        a = "buffalo"
        thislist = ["dog", "cat", "cow"]
        thislist.insert(1, "mouse")
        print(thislist)

        thislist.pop(2)
        print(thislist)
        thislist.append(a)
        print(thislist)

    animals()

# /replace item direct method


thislist = ["Docklands", "Flinders", "collins"]
thislist[2] = "coburg"
print(thislist)


class ind():
    def neg():
        mylist = ["apple", "cherry", "berry"]
        print(mylist[1:2])

    neg()

# check if item exists
    def fruit():
        pack = ["mango", "cherry", "grapes"]
        if "mango" in pack:
            print("yes, mango is in the list")
    fruit()


# extend list
pack = ["mango", "cherry", "grapes"]
mylist = ("kiwi", "apples")
pack.extend(mylist)
print(pack)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(2):
    print(thislist[i])
    print("value of i is :"+str(i))

#   for loop
mylist = ["car", "Jeep", "truck"]
for i in range(1):
    print(mylist[i])

# while loop

mylist = ["car", "Jeep", "truck"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

# list comprehension

veh = ["car", "Jeep", "truck"]
newlist = []
for x in veh:
    if "a" in x:
        newlist.append(x)
print(newlist)


# reverse
thislist = ["apple", "banana", "cherry"]
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n-50)


a = [20, 40, 60, 80]
a.sort(key=myfunc)
print(a)


a = ["veggie", "fruits"]
b = a.copy()
print(b)


def mynew():
    a = ["veggie"]


print(b)

mynew()


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list2.extend(list1)
print(list2)

# tuple

mytuple = ("kiwi", "lime", "orange")
y = list(mytuple)
y.append("mango")
mytuple = tuple(y)
print(mytuple)


car = {
    "Brand": "Honda",
    "Model": "CRV",
    "year": "2020"
}

x = car.keys()
car.values()
car.get("Brand")
car["color"] = "white"
print(x)

# check if  key exists

thisdict = {
    "brand": "Ford",
    "model": "Mustang"
}
y = thisdict.keys()
if "year" in y:
    print("yes")
else:
    print("no")

    # function


def myfunc(firstname, lastname):
    print(firstname + " "+lastname)


myfunc("Emil", "Tobias")
myfunc("rick", "glen")


def func(country="India"):
    print("I am from" + country)


func("Brazil")
func()
func("UK")


f = open("demotext.txt", "r")
print(f.read())

x = 1
y = 6
