f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

# with santax
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
with open("demo.txt", "w") as f:
    f.write("its javascript time")

