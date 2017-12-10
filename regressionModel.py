# -*- coding: utf-8 -*-
"""

"""




    #Data preprocessing

    #Importing libraries
import numpy as np
import pandas as pd
def regression(option_selected,bedroom,bathroom,area):
    #Importing the dataset
    dataset = pd.read_csv('RealEstateCSV.csv')


    #creating a matrix of independent variables/features
    x = dataset.iloc[ : , :-1].values
    #for dependent variable
    y = dataset.iloc[ : , 4].values



    '''
    #taking care of missing data

    from sklearn.preprocessing import Imputer
    imputer = Imputer(missing_values ='NaN',strategy = 'mean',axis =0)
    imputer = imputer.fit(x[ : ,-1:])
    x[:,-1:] = imputer.transform(x[:,-1:])
    '''
    #encoding categorical data
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_x = LabelEncoder()
    x[:,0]=labelencoder_x.fit_transform(x[:,0])
    onehotencoder = OneHotEncoder(categorical_features = [0])
    x = onehotencoder.fit_transform(x).toarray()

    #creating a copy of x will be used in feature scaling of the single sample later
    from copy import deepcopy
    other_x = deepcopy(x)


    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()

    x = sc_x.fit_transform(x)

    '''
    #splitting the dataset into Training and test set
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state = 0)
    '''


    '''
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(x_train,y_train)

    from sklearn.tree import DecisionTreeRegressor
    regressor_dt = DecisionTreeRegressor(random_state=0)
    regressor_dt.fit(x_train,y_train)
    '''

    '''
    # Fitting SVR to the dataset
    from sklearn.svm import SVR
    regressor = SVR(kernel = 'rbf')
    regressor.fit(x_train, y_train)
    '''

    #training the RandomForest model
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 325, random_state = 0)
    regressor.fit(x,y)

    #testing
    #y_pred = regressor.predict(x_test)

    '''
    from sklearn.metrics import mean_absolute_error
    accuracy = mean_absolute_error(y_test,y_pred)
    print("Accuracy of the prediction: ",accuracy)
    '''

    # fuction to predict land evaluations based on values of parameters given by user

    input_data = []
    '''
    option_selected =3
    bedroom = float(3)
    bath = float(3)
    area = float(4000)
    '''
    for i in range(0,15):
        if i == option_selected:
            input_data.append(float(1))
        else:
            input_data.append(float(0))

    input_data.append(bedroom)
    input_data.append(bathroom)
    input_data.append(area)

    input_data=np.asarray(input_data)

    other_x = np.vstack([other_x,input_data])

    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_otherx = StandardScaler()

    other_x = sc_otherx.fit_transform(other_x)

    input_data = other_x[-1]
    data = input_data


    input_data = np.vstack([input_data,data])
    #input_data = sc_x.fit_transform(input_data)

    prediction = regressor.predict(input_data[:])
    return (prediction[0])
