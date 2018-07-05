gandalf="Gandalf should fly"
stepr="steps right and"
stepl="steps left and"
f="forward"
b="backwark"
sumRL=int(0)
sumFB=int(0)
while True:
    turnRL=input("Next Turn:")
    if (turnRL=="end"):
        break
    countRL=int(input("How many steps?",))
    if (turnRL=="right"):
        sumRL+=countRL
        turnFB=input("Next turn:")
        countFB=int(input("How many steps?"))
        if (turnFB=="end"):
            break
        elif (turnFB=="left"):
            sumFB+=countFB
        else:
            sumFB-=countFB
    if (turnRL=="left"):
        sumRL-=countRL
        turnFB=input("Next turn:")
        countFB=int(input("How many steps?"))
        if (turnFB=="end"):
            break
        elif (turnFB=="left"):
            sumFB-=countFB
        else:
            sumFB+=countFB
if (sumFB>=0):
    if (sumRL>=0):
        print(gandalf, (sumRL),stepr, (sumFB) ,f)
    else:
        print(gandalf, (-sumRL),stepl, (sumFB),f)
else:
    if (sumRL>=0):
        print(gandalf, (sumRL), stepr, (-sumFB), b)
    else:
        print(gandalf, (-sumRL), stepl, (-sumFB), b)
