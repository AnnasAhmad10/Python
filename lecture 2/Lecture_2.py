str1 = "i am annas ahmad. \ni belongs to sherkhani. \ti am a student of apnacollege."
print(str1) #\n means next line, \t means tab space
str1 = "being"
str2 = "creative"
final_str = str1 + " " + str2 #this is concatenation
print(len(final_str)) #finding lenth of string

#indexing
str = "being creative"
print(str[3])
print(str[4])

#slicing
str = "being creative"
print(str[2: 7])

#string functions
str = "my facebook is being creative"
print(str.endswith("ive")) #str.endswith
print(str.endswith("ion"))
print(str.capitalize())    #str.capitalize
print(str.replace("ive" , "ion")) #str.replace
print(str.find("ion"))
print(str.find("i"))      #str.find
print(str.count("e"))     #str.count

#conditional statements
age = 22
if(age >= 18):
    print("can vote")    #if condition
elif(age < 18):
    print("cannot vote")   #elif = else if

light = "black"

if(light == "green"):
    print("go")
elif(light == "yellow"):
    print("ready")          #indentation = proper spacing
elif(light == "red"):
    print("stop")
else:
    print("light is broken")    #else condition

#building a marking system
marks = int(input("marks of the student is:"))
if(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B" 
elif(marks < 80 and marks >= 70):
    grade = "C"
elif(marks < 70):
    grade = "F"
print("grade of the student ->" , grade) 

#nesting
age = int(input("enter your age:"))
if(age >= 18):
    if(age >= 80):
        print("cannot drive")     
    else:
        print("can drive")
