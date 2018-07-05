Riders=int(input("Enter number of riders:"))
print("How tall is the hat?")
largest=0
for i in range(Riders):
    x=int(input())
    if (x>largest):
        largest=x
        position=int(i)
print("Gandalf's position is:",position+1)
