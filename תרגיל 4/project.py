'''
present:Elad Fisher , id:213924624
Yehoshua Gronpect, id:332521103

The following program classifies a group of points and then calculates
 the accuracy based on another file with the same data
 The program does so by calculating the distance from a point to other points
 The distance is calculated in three ways: Euclidian, Manhattan and Hamming
 We then checked how accurate each distance is when we change the amount of neighbors that we check


 NOTE NOTE NOTE NOTE NOTE:
 the answers are below, in the end (around line 350)
'''
import math
import csv
import string

class distClass:
    dist = -1 #distance of current point from test point
    tag = '-' #tag of current point

#function that print a vector in the way that they asked
def print_vector(vector):
    length = len(vector)-1
    result ="The vector ["
    for i in range (length) :
        result += str(vector[i])
        if i != length -1:
            result += ", "
    result+="] has tag "
    result+= str(vector[length])
    print(result)

#calculate the distance in the euclidian way.
def euclideanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         #print ('x is ' , x)
         num1=float(instance1[x])
         num2=float(instance2[x])
         distance += pow(num1-num2, 2)
   return math.sqrt(distance)

#open the file:"myFile", flag is to know whether you want the header or not
def open_document(flag):

    with open('myFile.csv', 'r') as myCsvfile:
        lines = csv.reader(myCsvfile)
        dataWithHeader = list(lines)

    # put data in dataset without header line
    if(flag):
        dataset = dataWithHeader[1:3]

    else:
        dataset = dataWithHeader[1:]

    return dataset

#open the file:"mytest"
def open_mytest():
    with open('mytest.csv', 'r') as myCsvfile:
        lines = csv.reader(myCsvfile)
        dataWithHeader = list(lines)
        dataset = dataWithHeader[1:]

    return dataset

#open the file:"mytrain"
def open_mytrain():
    with open('mytrain.csv', 'r') as myCsvfile:
        lines = csv.reader(myCsvfile)
        dataWithHeader = list(lines)
        dataset = dataWithHeader[1:]

    return dataset

# calculate and return list of eucDistances and the match tag
#from a dataset to the point
def distance(dataset ,point):
    eucDistances = []  # list of distances, will hold objects of type distClass
    for row in dataset:
        temp = row
        label = temp[-1]
        d = euclideanDistance(point, temp, len(point)-1)
        print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        print(" and the label is " + label)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        eucDistances.append(obj)

    return eucDistances

#write the new information after modify
def answer(file_name,dataWithHeader):
    with open(file_name+'.csv ', 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(dataWithHeader)

#return the tag, the parameters are the list of distances and the k
def tag(distList,point,k):
    male=0
    female=0

    for row in distList[0:k]:
        if row.tag == "M" :
            male += 1

        elif row.tag == "F" :
            female += 1

        else:
            return "you are idiot"

    if male > female:
        return"M"

    else:
        return"F"

#do classification to the file my_file
def classification_my_file(k):
    with open('myFile_test.csv', 'r') as myCsvfile2:
        lines = csv.reader(myCsvfile2)
        dataWithHeader = list(lines)
    dataset = open_document(False)

    point = dataWithHeader[1][:3]
    distList = distance(dataset, point)
    distList.sort(key=lambda x: x.dist)
    dataWithHeader[1][3] = tag(distList,point,k)

    point = dataWithHeader[2][:3]
    distList = distance(dataset, point)
    distList.sort(key=lambda x: x.dist)
    dataWithHeader[2][3] = tag(distList,point,k)

    with open('myFile_test.csv ', 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(dataWithHeader)

#learn and classified the file mytest using euc distance and return the accuracy
def myteste(k,name):
    dataset_learn = open_mytrain()
    dataset_test = open_mytest()

    right = 0
    wrong = 0
    mytest1e_dataset = dataset_test

    length = len(mytest1e_dataset[1])
    for i in range(len(dataset_test)):
        p = dataset_test[i]
        print(point)
        distList = distance(dataset_learn, p)
        distList.sort(key=lambda x: x.dist)
        mytest1e_dataset[i][length - 1] = tag(distList, point, k)

    answer(name , mytest1e_dataset)

    for i in range(len(mytest1e_dataset)):
        dataset_test = open_mytest()
        if (dataset_test[i][length - 1] == mytest1e_dataset[i][length - 1]):
            right += 1

        else:
            wrong += 1

    return right/(right+wrong)

#calculate the manhatan distance between 2 points
def manhatan(instance1,instance2,length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += abs(num1 - num2)
    return distance

#return the list of  manhatan distances and their tag from a point
def Mdistance(dataset ,point):
    manDistances = []  # list of distances, will hold objects of type distClass
    for row in dataset:
        temp = row
        label = temp[-1]
        d = manhatan(point, temp, len(point)-1)
        print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        print(" and the label is " + label)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        manDistances.append(obj)

    return manDistances

#learn and classified the file mytest using manhatan distance and return the accuracy
def mytestm(k,name):
    dataset_learn = open_mytrain()
    dataset_test = open_mytest()

    right = 0
    wrong = 0
    mytest1e_dataset = dataset_test

    length = len(mytest1e_dataset[1])
    for i in range(len(dataset_test)):
        p = dataset_test[i]
        print(point)
        distList = Mdistance(dataset_learn, p)
        distList.sort(key=lambda x: x.dist)
        mytest1e_dataset[i][length - 1] = tag(distList, point, k)

    answer(name, mytest1e_dataset)

    for i in range(len(mytest1e_dataset)):
        dataset_test = open_mytest()
        if (dataset_test[i][length - 1] == mytest1e_dataset[i][length - 1]):
            right += 1

        else:
            wrong += 1

    return right / (right + wrong)

#calculate the hamming distance between 2 points
def hamming (instance1,instance2,length):
    distance = 0
    for x in range(length):
        # print ('x is ' , x)
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        if(num1 != num2):
            distance += 1
    return distance

#return the list of hamming distances and their tag from a point
def Hdistance(dataset ,point):
    HDistances = []  # list of distances, will hold objects of type distClass
    for row in dataset:
        temp = row
        label = temp[-1]
        d = hamming(point, temp, len(point) - 1)
        print("The distances between " + str(point) + " and " + str(temp) + " is " + str(d))
        print(" and the label is " + label)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        HDistances.append(obj)

    return HDistances

#learn and classified the file mytest using hamming distance and return the accuracy
def mytesth(k,name):
    dataset_learn = open_mytrain()
    dataset_test = open_mytest()

    right = 0
    wrong = 0
    mytest1e_dataset = dataset_test

    length = len(mytest1e_dataset[1])
    for i in range(len(dataset_test)):
        p = dataset_test[i]
        print(point)
        distList = Hdistance(dataset_learn, p)
        distList.sort(key=lambda x: x.dist)
        mytest1e_dataset[i][length - 1] = tag(distList, point, k)

    answer(name, mytest1e_dataset)

    for i in range(len(mytest1e_dataset)):
        dataset_test = open_mytest()
        if (dataset_test[i][length - 1] == mytest1e_dataset[i][length - 1]):
            right += 1

        else:
            wrong += 1

    return right / (right + wrong)

#the points from part 1 of the exersize
point = [1, 0, 0, '?']
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']

print_vector(point)
print_vector(data1)
print_vector(data2)

#they asked us to print this distance
print(euclideanDistance(data1,data2,len(data1)-1))

dataset = open_document(True)

print_vector(dataset[0])
print_vector(dataset[1])
print(euclideanDistance(dataset[0],dataset[1],len(dataset[0])-1))

dataset = open_document(False)
distList = distance(dataset,point)

distList.sort(key=lambda x: x.dist)

for row in distList:
    print (row.tag)

print(" ")
print(tag(distList,point,1))
print(tag(distList,point,3))
classification_my_file(3)

# part 2:(the comment is the accuracy after we run this program)

#mytest1e
accuracy = []
accuracy.append(myteste(1,"mytest1e"))#0.5
accuracy.append(myteste(7,"mytest7e"))#0.74
accuracy.append(myteste(19,"mytest19e"))#0.68

#mytest1m
accuracy.append(mytestm(1,"mytest1m"))#0.61
accuracy.append(mytestm(7,"mytest7m"))#0.63
accuracy.append(mytestm(19,"mytest19m"))#0.7

#mytest1H
accuracy.append(mytesth(1,"mytest1h"))#0.61
accuracy.append(mytesth(7,"mytest7h"))#0.55
accuracy.append(mytesth(19,"mytest19h"))#0.56


print(accuracy)

'''
answers:
part 1:
F,F

2)a)0.5
 b)0.74
 c)0.68
 d)7
 
 g)euclidian with k=7 give us 74 percent accuracy

'''








