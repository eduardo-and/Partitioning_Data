import numpy as np
import pandas as pd
import math

def partData(data,target=[],test_percentage=0.3):
    
    def targetExtract(data,tp):
        size= data.shape[1]
        if(tp==1):
            target= data[size-1]
            
            data= data.iloc[:,:size-1]
            return data, target
        
        else:                    
            
            target= data[-1]
            data=data[:len(data)-1]
            return data,target    
                
    def insertTarget(data,target):
        colSize= data.shape[1]
        data.insert(loc= colSize,value=target,column=colSize)
        return data
   
    # Define data type
    if(isinstance(data,np.ndarray) or type(data)== list):
        if(isinstance(data,np.ndarray)):
            data = data.tolist()
        if(isinstance(target,np.ndarray)):    
            target = target.tolist()
        tp= 0
    elif(isinstance(data,pd.core.frame.DataFrame)):
        tp= 1
    else:
        return False
    
    
    if(tp!=1):
        data = pd.DataFrame(data)
           
    if(target != []):
        data = insertTarget(data,target)
          
    
    part = 1 - test_percentage # Porcentagem de dados que vão para o treino
    colSize= data.shape[1] # Quantidade de colunas do dataframe
    linSize= data.shape[0] # Quantidade de Linhas do dataframe
    classes = len(set(data[colSize-1])) # Quantidade de classes do dataframe
    rangeClass = dict() 
    
    
    data = data.sort_values(colSize-1).reset_index(drop=True) #Ordena os dados

    for line in range(linSize):   # Cria um dicionário com keys= classe value= índice do última elemento com a classe em questão
        final= data[colSize-1][line]
        rangeClass[final]= line
   
    keys= list(rangeClass.keys()) # Variável com a lista de chaves
    newData= dict() # Dicionário que receberá os dados divididos por classe
    
    for line in range(classes): # Divide os dados por classes em um dicionário
        final= rangeClass[keys[line]]    
        if(line==0):
            newData[keys[line]]= data[:final+1]
        else:
            start= rangeClass[keys[line-1]]+1
            newData[keys[line]]= data[start:final+1]
    

    qt= []    # Quantidade de dados(por classe)
    qtTraining = [] # Quantidade de dados que vão compor o dataset de treino
       
    
    for line in range(classes):     # Extrai a quantidade de linhas em cada classe e calcula quantas serão para o treinamento
        qt.append(newData[keys[line]].shape[0])
        qtTraining.append(math.ceil(qt[line]*part))


    #qtTest = [num-qtTraining[cont] for cont,num in enumerate(qt)]


    for line in range(classes): # Realiza a criação dos novos dados de treino e teste, balanceados com a mesma porcentagem de cada classe 
        
        if(line==0):
            training_sample = newData[keys[line]][:qtTraining[line]].values.tolist() # Cria e inicia a lista que ira compor o novo dataframe de treino
            test_sample = newData[keys[line]][qtTraining[line]:].values.tolist() # Cria e inicia a lista que ira compor o novo dataframe de teste
            continue
        temp = newData[keys[line]][:qtTraining[line]].values.tolist() 
        temp2 = newData[keys[line]][qtTraining[line]:].values.tolist() 
        
        for uni in temp: # Adiciona valores a lista de dados de treino
            training_sample.append(uni)
        
        for uni in temp2: # Adiciona valores a lista de dados de teste
            test_sample.append(uni)

    training_sample =  pd.DataFrame(training_sample) #Cria o novo dataframe de treino
    test_sample =  pd.DataFrame(test_sample) #Cria o novo dataframe de teste
    tr_sample, tr_target =  targetExtract(training_sample,1)
    test_sample, test_target = targetExtract(test_sample,1)
    
    return tr_sample,np.array(tr_target),test_sample,np.array(test_target)
