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
            counter=0
            iterations+=1
            for j in range(0,n):
                w[j]=(labels[i]*(data[i][j]))+w[j]
            b-=labels[i]
        else:
            counter+=1
        if counter==m:
            return(w,b)
        i+=1
        if (i==m):
            i=0

def generalization_error(data, labels, w, b):
    m=len(data)
    n=len(data[0])
    checklist=([0]*m)
    for i in range(0,m):
        sign=dot(w,data[i])-b
        if ((sign>=0 and labels[i]<0)or(sign<0 and labels[i]>=0)):
            checklist[i]=1
        else:
            checklist[i]=0
    return checklist
            
        
    


def vector_to_matrix(vec):
    size=5
    matrix=[[0 for x in range(5)] for x in range(5)]
    for i in range(0,size):
        for j in range(0,size):
            matrix[i][j]=vec[j+(i*size)]
    return (matrix)
 

def classifier_4_7(data, labels):
    w=[0]*784
    b=[0]*784
    for i in range(0,784):
        new_list=perceptron(data[i],labels[i])
        w[i]=new_list[0]
        b[i]=new_list[1]

def test_4_7(train_data, train_labels, test_data, test_labels):
    pass


yos=[5,2,5,4,4,3,3,2,5,6,3,12,644,5,2,0,23,1,5,8,6,5,3,1,5]
mat=vector_to_matrix(yos)
print(yos)
print(mat)
