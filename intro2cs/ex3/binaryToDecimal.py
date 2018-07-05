binary=int(input("Insert number in binary representation:",))
i=int(0)
decimal=int(0)
while (binary!=0):
    if (binary%10==1):
        decimal+=int(2**i)
    binary=int(binary/10)
    i+=1
print("The decimal value of the inserted binary number is", decimal)
