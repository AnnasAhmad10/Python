#listing in python
marks = [90 , 80, 48, 92, 56]
print(marks)
marks[1] = 82
print(marks)

#slicing of list = same as slicing of string

#list methods
list = [67, 78, 65, 92]
list.append(81)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(2, 78)
print(list)
list.remove(81)
print(list)
list.pop(4)
print(list)

#tuples = just like str in paranthesis but must be represented with comma, and like list in writing.
tup = (1, 2, 3, 4)
print(tup)

#slicing is same as list and string
print(tup[2 : 5])
#tuple methods
#1)tup.index 
#2)tup.count
print(tup.index(3))
print(tup.count(2))
