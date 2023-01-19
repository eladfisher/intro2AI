from sklearn import tree

from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt

from sklearn import datasets

# import some data to play with

iris = datasets.load_digits()

# mylist = []
# do loop
X_accuracy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
X_precision = []
X_recall = []
X_f1 = []
for i in range(10):
    clf = tree.DecisionTreeClassifier()

    clf.max_depth = i + 1

    clf.criterion = 'entropy'

    clf = clf.fit(iris.data, iris.target)

    print("Decision Tree: ")

    #accuracy
    accuracy = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
    X_accuracy[i] = round(accuracy.mean(), 3) ** 2
    print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(), 3))

    # mylist.append(accuracy.mean())  loop, can be used to plot later…
    #precision
    precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
    X_precision.append(round(precision.mean(), 3) ** 2)
    print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))

    #recall
    recall = cross_val_score(clf, iris.data, iris.target, scoring='recall_weighted', cv=10)
    X_recall.append(round(recall.mean(), 3) ** 2)
    print("Average recall of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))

    # f1
    f1 = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)
    X_f1.append(round(f1.mean(), 3) ** 2)
    print("Average recall of  DT with depth ", clf.max_depth, " is: ", round(f1.mean(), 3))

    print("   ")

best_accuracy = 0
for depth in range(10):
    if X_accuracy[depth] >X_accuracy[best_accuracy]:
        best_accuracy = depth

print("the best accuracy is for depth of",best_accuracy+1)

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(X_accuracy)

plt.plot(X, X_accuracy)
plt.xlabel("This is the NODES axis")
plt.ylabel("This is the X_accuracy_digit axis")
plt.show()

plt.plot(X, X_precision)
plt.xlabel("This is the X axis")
plt.ylabel("This is the X_precisio_digit axis")
plt.show()

plt.plot(X, X_recall)
plt.xlabel("This is the X axis")
plt.ylabel("This is the X_recal_digit axis")
plt.show()

plt.plot(X, X_f1)
plt.xlabel("This is the X axis")
plt.ylabel("This is the X_f1_digit")
plt.show()
