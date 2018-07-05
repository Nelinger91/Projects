#############################################################
# FILE : ex5.py
# WRITER : your_name , your_login ,
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# Enter description.
#
#############################################################
"""
implement the methods below (replace the pass statement with the code),
and add their docstrings.
"""

def dot(A, B):
    n=len(A)
    sum=0
    for i in range(0,n):
        sum+=A[i]*B[i]
    return sum


def perceptron(data, labels):
    m=len(data)
    n=len(data[0])
    w=list([0]*n)
    b=0
    counter=0
    iterations=0
    i=0
    sign=0
    while True:
        if iterations==10**m:
            return(None,None)
        dot_product=dot(w,data[i])-b
        if dot_product>=0:
            sign=1
        else:
            sign=-1
        if sign!=labels[i]:
            iterations+=1
            for j in range(0,n):
                w[j]+=labels[i]*(data[i][j])
            b-=labels[i]
        else:
            counter+=1
        if counter==m:
            return(w,b)
        i+=1
        if (i==m):
            i=0

def generalization_error(data, labels, w, b):
    pass


def vector_to_matrix(vec):
    pass
 

def classifier_4_7(data, labels):
    pass


def test_4_7(train_data, train_labels, test_data, test_labels):
    pass

info=[(1,1,6),(2,4,2),(3,4,0),(6,5,2),(6,2,1),(3,3,3)]
tagit=[-1,1,-1.0,1,1.0,-1]
print(perceptron(info,tagit))

