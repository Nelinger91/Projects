import intro2cs_ex5
import perceptron 

data = intro2cs_ex5.loadtxt('data.txt')
labels = intro2cs_ex5.loadtxt('labels_AND.txt')

(w,b) = perceptron.perceptron(data,labels)
print(w,b)
errors= generalization_error(data,labels,w,b)
