print ("insert weights one by one")
weight=0
sum=0
while (weight!=-1):
    weight=int(input())
    if weight==-1:
        break
    elif weight>0:
        sum+=weight
    elif weight<0:
        print("Weights must be non-negative")
    if sum>100:
        print("Overweight!Gandalf will not approve")
        break
if sum<100:
    print ("the total packed weight is", sum)
        
