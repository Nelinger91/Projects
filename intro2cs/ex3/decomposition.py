composed=int(input("Insert composed number:"))
i=1
x=10
prevx=1
sentence="The number of goblets Gimli drank on day"
was="was"
while (x<=(composed*10)):
    decomposed=int((composed%x)/prevx)
    print (sentence,i,was,decomposed)
    prevx=x
    x*=10
    i+=1
