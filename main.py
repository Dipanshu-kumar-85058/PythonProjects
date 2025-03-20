# general print program

print("hello world")

# calculator using arithematic operations
a=int(input("a= "))
b=int(input("b= "))
p=a+b
q=a-b
r=a*b
s=a/b
t=a//b
u=a%b
op=str(input("Enter the operation: "))
if op=='+':
      print(p)
elif op=='-':
      print(q)
elif op=='*':
      print(r)
elif op=='/':
      print(s)
elif op=='//':
      print(t)
elif op=='%':
      print(u)
else:
      print("Invalid operation")


# stings
# string operations
x=str(input("name1 : "))
y=str(input("name2 : "))
print(x+y) # concatenation
print(x*2) # repetition
print(x[1])  # indexing
print(x[1:4])  # slicing
print(x[1:])  # slicing from 1 to end
print(x[:4])  # slicing from start to 4
print(x[-1])  # negative indexing
print(x[-4:-1])  # negative slicing from -4 to -1
print(len(x)) # length of string 

# string methods

print(x.upper())  
# upper case

print(x.lower())  
# lower case 

print(x.split())  
# split it splits the string

print(x.strip()) 
# strip it removes the white spaces

print(x.replace('h','j'))  
# replace it replaces the string

print(x.count('l'))  
# count it counts the number of occurences of the given character

print(x.find('l')) 
# find it finds the first occurence of the given character

print(x.islower())  
# islower it checks if all the characters are in lower case

print(x.isupper())  
# isupper it checks if all the characters are in upper case

print(x.startswith('h'))  
# startswith it checks if the string starts with the given character

print(x.endswith('o'))  
# endswith it checks if the string ends with the given character

print(x.capitalize()) 
# capitalize it converts the first character to upper case

print(x.title())
# title it converts the first character of each word to upper case

print(x.swapcase())
# swapcase it converts the upper case to lower case and vice versa

print(x.center(10)) 
# center it centers the string with the given width

print(x.partition('e'))
# partition it partitions the string with the given character

print(x.splitlines())
# splitlines it splits the string at the line breaks

print(x.encode())
# encode it encodes the string

print(x.expandtabs())
# expandtabs it expands the tabs

print(x.casefold())
# casefold it converts the string to lower case

print(x.replace('h','j'))
# replace it replaces the string
