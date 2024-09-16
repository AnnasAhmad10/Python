meaning ={
    "name" : "annas",
    "class" : "llb",
    "subjects" : ('pil', 'pil2'),
    "marks" : ["56", "26", "32"],
}

meaning["name"] = "jan sb"
meaning["surname"] = "akhunzada"


#nested dictionary
meaning1 ={
    "name" : "annas",
    "class" : "llb",
    "subjects" : {
        "pil" : 67,
        "pil2" : 88,
        "hr" : 78,
    },
    "marks" : ["56", "26", "32"],
}
 
 #dictionary methods
print(meaning1.keys())

print(meaning1.values())

student ={
    "name" : "annas",
    "class" : "llb",
    "subjects" : {
        "pil" : 67,
        "pil2" : 88,
        "hr" : 78,
    },
    "marks" : ["56", "26", "32"],
}
print(student)
new_dic = {"unit" : "A block"}
student.update(new_dic)
print(student)

#sets
version = {2,3,3,4,5}
print(type(version))
version.pop()
print(version)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))