x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    
x = 55
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

if x < 10:
    print("smaller than 10")

# these next couple take up a lot of room.  Messing with loops
# for x in range(0, -256, -1): # just manipulate the positive and negative to move the direction.
#     if(x%2==0):
#         print(x)
#     else:
#         print("skipping")

# for x in range(51):  # if we're incrementing by one and starting at 0 they both can be left out
#     print(x)

myList = ["abc", 123, "xyz", "purple"]
for i in range(0, len(myList)):
    print(i, myList[i], "is the item") #use comma with quotes instead of concatenating
    
for v in myList:
    print(v)
    
myDict = { "name": "Noelle", "language": "Python", "age": "24", "personality": "crazy!"}
for k in myDict:
    print(k,":", myDict[k]) #commas work here also
    #print(k)


capitals = {"Georgia": "Atlanta", "Texas": "Austin", "Montana": "Helena", "Washington": "Seattle"}

for key in capitals.keys():
    print(key)

for val in capitals.values():
    print(val)
    
for key, val in capitals.items():
    print(key, " = ", val)
    
count = 0
while count <= 5:
    print("looping - ", count)
    count+=1
    
y = 3
while y > 0:
    print(y)
    y = y -1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
    
for val in "string":
    if val == "i":
        continue
    print(val)
    
z = 3
while z > 0:
    print(z)
    z = z - 1
    if z == -1:
        break
else:
    print("Final else statement")