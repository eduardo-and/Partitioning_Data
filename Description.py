import partitioning_data as ptD

from sklearn import datasets 
from sklearn.linear_model import LogisticRegression as LR

# The library performs the partitioning of data, dividing in 4 parts:
# 1ª : Training sample
# 2ª : Training target
# 3ª : Teste smaple
# 4ª : Teste target
# The split is based on a percentage parameter of data that will go for testing.
#
# Function:
#
# - partData(data,target=False,test_percentage)
#
#   The function divides the data for training and testing, partitioning is done by separating the dataSet by classes,
#   and then creating the new training and test data with an equal proportion of classes for each new dataSet. 
#   
#   input: 
#       data : The dataset with or with out the data target. Accepted types: Array,List and DataFrame
#       target(optional): If your target is already in a single data, not is necessary inform this parameter. Accepted types: Array,List, Series.
#       test_percentage(optional): (Default: 0.30) The parcentage of data with will go to teste. Accepted values: 0,01 - 0,99
#   Output:
#       Training sample:
#            Type: DataFrame
#            Description: Sample data for training 
#
#       Training target:
#            Type: Array
#            Description: Sample target of data for training 
#
#       Teste smaple:
#            Type: DataFrame
#            Description: Sample data for test 
#
#       Teste target:
#           Type: DataFrame
#           Description: Sample target of data for training
#
#
# * Initially, this function is done for classification data, as the data is divided through class balancing.   


iris = datasets.load_iris() # Exemple dataset 
data, target = datasets.load_iris(return_X_y=True) # Import sample variable and target.
print(f'Sample Data:\n{data[:10]}\n\nTarget:\n{target[:10]}')

training_sample,training_target,test_sample,test_target = ptD.partData(data,target,0.30) # Partitioning of data

print("\n\nTraining data:\n")
print(training_sample.head)
print("\ntarget data of training:\n")
print(training_target)
print("\nTest data:\n")
print(test_sample.head)
print("\nTeste target data:\n")
print(test_target)


clf = LR(random_state=0,max_iter=500).fit(training_sample,training_target) # Exemple classification algorithm

print("Acuracy:") 
print(clf.score(test_sample,test_target))