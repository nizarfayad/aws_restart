#print("Python has three numeric types: int, float, and complex")
myValue=1
print(myValue)
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue = 3.14
print(myValue)
print(str(myValue) + " is of the data type" + str(type(myValue)))

myValue=5j
print(myValue)

print(type(myValue))
print(f"{myValue} is of the data type {type(myValue)}")


firstString="water"
secondString="fall"
thirdString = firstString + secondString
print(thirdString)

name = input("what is your name? ")
print(name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))
