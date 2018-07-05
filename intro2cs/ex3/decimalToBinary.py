decimal=int(input("Insert number in decimal representation:",))
temp=decimal
i=1
binary=int(0)
while (decimal>0):
    while (temp!=1):
        temp=int(temp/2)
        i+=1
    binary=binary+(10**(i-1))
    decimal=int(decimal-(2**(i-1)))
    i=1
    temp=decimal
print("The binary value of the inserted decimal number is", binary)
