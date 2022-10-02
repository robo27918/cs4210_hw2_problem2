#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# Note: made use of the strategy used in solutions of hw1 to convert features to integers
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
age = {
    "Young": 1,
    "Prepresbyopic": 2,
    "Presbyopic": 3,
}

spectacle = {
    "Myope": 1,
    "Hypermetrope": 2,
}

astigmatism = {
    "Yes": 1,
    "No": 2,
}

tear = {
    "Normal": 1,
    "Reduced": 2,
}
lenses = {
    "Yes": 1,
    "No": 2,
}
index = 0

#read the test data and add this data to dbTest
       #--> add your Python code here
dbTest = []
with open("contact_lens_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append (row)
#transform the features of the test instances to numbers following the same strategy done during training,
int_test_set = []
for instance in dbTest:
    int_test_set.append([age[instance[0]], spectacle[instance[1]], astigmatism[instance[2]],tear[instance[3]], lenses[instance[4]] ])

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)
    #print ("Values for dbTraining",": ",dbTraining  )
    #print("dbTraining data after reading file ", ds, ": ", dbTraining)
    #print(" # instances in the training set:", len(dbTraining))
   
    #print()
    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for instance in dbTraining:
        X.append([age[instance[0]], spectacle[instance[1]], astigmatism[instance[2]],tear[instance[3]] ])
   
   
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =
    for class_label in dbTraining:
         Y.append(lenses[class_label[4]])
    #loop your training and test tasks 10 times here
    accuracy = []
    for i in range(10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

     
      # for data in dbTest:
      #transform the features of the test instances to numbers following the same strategy done during training,
      #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
      #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
      #--> add your Python code here
       total_correct = 0
       for instance in int_test_set:
            #print("----Testing Phase ---- ")
            #print(instance[0:4])
            class_predicted = clf.predict([instance[0:4]])[0]
            #print("class_predicted: ",  class_predicted," True label: ", instance[4] ,"\n")
            actual_label = instance[4]
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            if class_predicted == actual_label:
                total_correct +=1
       accuracy.append(total_correct / len(int_test_set))
    #print ("accuracies for the 10 tests: ", accuracy)
    print ("Final accuracy when training on",ds,":",min (accuracy))
    #find the lowest accuracy of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    



