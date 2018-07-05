before=int(input("What is the age of the current dancer?" ))
current=int(input("What is the age of the current dancer?" ))
if (current>before):
    largest=current
    largestid=2
    pippen=int(1)
    pippenage=before
else:
    pippen=int(2)
    largest=before
    largestid=1
    pippenage=current
before=current
for i in range(3,11):
    current=int(input("What is the age of the current dancer?" ))
    if (current>pippenage and current<largest):
        pippen=int(i)
        pipenage=current
    elif (current>largest):
        pipenage=largest
        largest=current
        pippen=largestid
        largestid=i
print ("Pippin is dancer number",pippen)
