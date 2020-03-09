print("hel\tlo" , end = " ")
print("hello")
print("hello" + "world")
#This is a single lined comment

'''
Now onto variables in python
'''

x = 4;
xNew = "hello"
firstRealVariable = 21
secondRealVariable = 32
print("my first time manipulating variables equals" ,  firstRealVariable + secondRealVariable)
print ("x =", x)

booleanTest = False
print("the following is not true," , "so, " , booleanTest)
print(3/4)
print("I want floor division", 3//4)
print("Doing exponents only requires two stars, for example 5^2 is written as 5**2, which equals", 5**2)
print("Modulo is written normally" , 4%2)
y = 3.5
print(y)

#An example of casting
y = int (3.5)
print("y casted as an int", y)
z = max(4,5)
print(z)


# x = input("Please enter a number for the scanner test: ")

print("you entered: ", x)
s = "input"
# The length of a variable uses the function len(Variable)
print(len(s))

'''To get a substring you use  this format. sub = "SubstringTest" is the variable, so
to get the substring from 0 to 2 we do sub[0:3] 
'''
s = "substring"
print(s[0:3])

#If I want the last 3 letters of a string, say my "substring" string, use negative then the number of indexes
print(s[-4:])

#The Python version of contains() which returns boolean
print("This character is in the string:", "p" in s)

'''
ArrayLists in Python are list = [], it seems as long as you have the word
list in there you can add the variable name to the back or front of it 
and it will still work
'''

firstList = []
firstList.append("hello")
firstList.append("Guten Tak")
firstList.append("Hola como estas")

print(firstList)
print("The length of my list is: ",len(firstList))


