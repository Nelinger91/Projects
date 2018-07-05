orc=int(input("Which Orc do you wish to confront?"))
if (orc==1 or orc==2):
    print ("The required number of arrows is 1")
orcA=(1)
orcB=(1)
for i in range(2,orc):
    arrows=orcA+orcB
    orcA=orcB
    orcB=arrows
print ("The required number of arrows is:", arrows)
           
