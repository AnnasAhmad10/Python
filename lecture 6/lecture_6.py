#while loop
count = 8
while count >= 1:
    print("pakistan", count)
    count -= 1

    count = 1
while count >= 8:
    print("pakistan", count)
    count += 1

    #making table in loops

n = int(input("enter digit:"))
i = 1
while i <= 10:
    print(n*i)
    i+=1

nums = [1,4,9,16,25,36,49,64,81,100]
teachers = ["khatana", "rauf","ali"]
i = 0
while i < len(teachers):
    print(teachers[i])
    i  += 1 

nums = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("found in idx:", i)
    else:
        print("not found")
        i += 1

#break and continue keywords
i = 1

while i <=8:
    if(i == 3):
        i +=1
        continue
    print(i)
    i += 1

#For loop 
nums = [1,2,3,4,5]
for words in nums:
    if(nums == 3):
        continue
    print(words)
    #range in for loop

for i in range(10):
    print(i)