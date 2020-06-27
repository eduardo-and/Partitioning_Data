# Partitioning Data
**Author:** Eduardo de Andrade;

**Languages/Tools/Frameworks:** Python
 
**Date:** 27/06/2020

**Description:**
The library performs the partitioning of data, dividing in 4 parts:
  - 1ª : Training sample
  - 2ª : Training target
  - 3ª : Teste smaple
  - 4ª : Teste target<br><br>

The split is based on a percentage parameter of data that will go for testing. Initially, this function is done for classification data, 
as the data is divided through class balancing.  

### **Run:**
  - #### 1. Move the file partitioning_data.py for inside of your python project and import the library in the file you want to use the library:<br>
              
             import partitioning_data as ptD #Or a name of your choice
                      
              
  - #### 2.Use the function partData. The library contains just 1 function:
    ###  **partData(data,target=False,test_percentage)**
            
       The function divides the data for training and testing, partitioning is done by separating the dataSet by classes,
        and then creating the new training and test data with an equal proportion of classes for each new dataSet.**
    
       **Input:** <br>
             &nbsp;&nbsp; - **data :** The dataset with or with out the data target. Accepted types: Array,List and DataFrame.<br> <br>
             &nbsp;&nbsp; - **target(optional):** If your target is already in a single data, not is necessary inform this parameter. Accepted types: Array,List, Series.<br><br>
             &nbsp;&nbsp; - **test_percentage(optional):** (Default: 0.30) The parcentage of data with will go to teste. Accepted values: 0,01 - 0,99<br><br>
       **Return:** <br>
       - **Training sample:** <br>
          &nbsp; - *Type:* DataFrame<br>
          &nbsp; - *Description:* Sample data for training <br>

       - **Training target:** <br>
           &nbsp; - *Type:* Array<br>
           &nbsp; - *Description:* Sample target of data for training <br>

       - **Teste smaple:**<br>
           &nbsp; - *Type:* DataFrame<br>
           &nbsp; - *Description:* Sample data for test <br>

       - **Teste target:**<br>
          &nbsp; - *Type:* DataFrame<br>
          &nbsp; - *Description:* Sample target of data for training <br>


     >
### **Exemple:**
        
  &nbsp;&nbsp; **Import and define Dataset:**
               
              import partitioning_data as ptD

              from sklearn import datasets 
              
              iris = datasets.load_iris() # Exemple dataset 
              data, target = datasets.load_iris(return_X_y=True) # Import sample variable and target.
              print(f'Sample Data:\n{data[:10]}\n\nTarget:\n{target[:10]}')
              
&nbsp;&nbsp;**Original Data(reduced):**
   
                Sample Data:
                  [[5.1 3.5 1.4 0.2]
                   [4.9 3.  1.4 0.2]
                   [4.7 3.2 1.3 0.2]
                   [4.6 3.1 1.5 0.2]
                   [5.  3.6 1.4 0.2]
                   [5.4 3.9 1.7 0.4]
                   [4.6 3.4 1.4 0.3]
                   [5.  3.4 1.5 0.2]
                   [4.4 2.9 1.4 0.2]
                   [4.9 3.1 1.5 0.1]]

                  Target:
                  [0 0 0 0 0 0 0 0 0 0]
                  
 &nbsp;&nbsp;  **Using the function partData for partitioning the Dataset :**
                              
                training_sample,training_target,test_sample,test_target = ptD.partData(data,target,0.30) # Partitioning of data
      

&nbsp;&nbsp;  **New variables after the partitioning:**
  
                  print("Training data:\n")
                  print(training_sample)
                  print("\ntarget data of training:\n")
                  print(training_target)
                  print("\nTest teste:\n")
                  print(test_sample)
                  print("\nTeste target data:\n")
                  print(test_target)
    
   &nbsp;&nbsp;**Output:**
   
                  Training data:

                    <bound method NDFrame.head of        0    1    2    3
                    0    5.1  3.5  1.4  0.2
                    1    5.2  3.5  1.5  0.2
                    2    5.2  3.4  1.4  0.2
                    3    4.7  3.2  1.6  0.2
                    4    4.8  3.1  1.6  0.2
                    ..   ...  ...  ...  ...
                    100  6.5  3.0  5.8  2.2
                    101  7.6  3.0  6.6  2.1
                    102  4.9  2.5  4.5  1.7
                    103  7.3  2.9  6.3  1.8
                    104  6.7  2.5  5.8  1.8

                    [105 rows x 4 columns]>

                  Target data of training:

                    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
                     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
                     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2. 2.
                     2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.
                     2. 2. 2. 2. 2. 2. 2. 2. 2.]

                  Test data:

                    <bound method NDFrame.head of       0    1    2    3
                    0   4.9  3.1  1.5  0.1
                    1   5.4  3.7  1.5  0.2
                    2   4.8  3.4  1.6  0.2
                    3   5.0  3.4  1.5  0.2
                    4   5.1  3.7  1.5  0.4
                    5   4.3  3.0  1.1  0.1
                    6   5.8  4.0  1.2  0.2
                    7   5.7  4.4  1.5  0.4
                    8   5.4  3.9  1.3  0.4
                    9   5.1  3.5  1.4  0.3
                    10  5.7  3.8  1.7  0.3
                    11  5.1  3.8  1.5  0.3
                    12  5.4  3.4  1.7  0.2
                    13  4.8  3.0  1.4  0.1
                    14  4.6  3.6  1.0  0.2
                    15  5.2  2.7  3.9  1.4
                    16  5.0  2.0  3.5  1.0
                    17  5.9  3.0  4.2  1.5
                    18  7.0  3.2  4.7  1.4
                    19  6.1  2.9  4.7  1.4
                    20  5.6  2.9  3.6  1.3
                    21  6.7  3.1  4.4  1.4
                    22  5.6  3.0  4.5  1.5
                    23  5.8  2.7  4.1  1.0
                    24  6.2  2.2  4.5  1.5
                    25  5.6  2.5  3.9  1.1
                    26  5.9  3.2  4.8  1.8
                    27  6.1  2.8  4.0  1.3
                    28  6.3  2.5  4.9  1.5
                    29  6.0  2.2  4.0  1.0
                    30  7.2  3.6  6.1  2.5
                    31  6.3  2.7  4.9  1.8
                    32  6.5  3.2  5.1  2.0
                    33  6.2  3.4  5.4  2.3
                    34  5.7  2.5  5.0  2.0
                    35  5.8  2.8  5.1  2.4
                    36  6.4  3.2  5.3  2.3
                    37  6.5  3.0  5.5  1.8
                    38  7.7  3.8  6.7  2.2
                    39  7.7  2.6  6.9  2.3
                    40  6.0  2.2  5.0  1.5
                    41  6.9  3.2  5.7  2.3
                    42  5.6  2.8  4.9  2.0
                    43  6.4  2.7  5.3  1.9
                    44  5.9  3.0  5.1  1.8>

                   Teste target data:

                    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.
                     1. 1. 1. 1. 1. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]

   &nbsp;&nbsp;**Exemple in classification algorithm:**
                
                from sklearn.linear_model import LogisticRegression as LR
                
                clf = LR(random_state=0,max_iter=500).fit(training_sample,training_target) # Exemple classification algorithm
                print("Acuracy:") 
                print(clf.score(test_sample,test_target))
      
  &nbsp;&nbsp;Output:
              
                Acuracy: 0.9555555555555556
     
**To run the examples on your machine, move the files description.py and partitioning_data.py into your project and run description.py.**
