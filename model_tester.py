# model_tester.py
# tests the house sorting model with agruments on the command line
# usage: python3 model_tester.py <EXT Score> <AGR Score> <CSN Score> <OPN Score>

# imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 	
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import sys

def main():
    # import CSV
    data = pd.read_csv('Data/scores_sorted.csv')

    # read scores to test from command line
    #args = [[sys.argv[1]], [sys.argv[2]], [sys.argv[3]], [sys.argv[4]]]
    args = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    #input_data = pd.DataFrame(args, columns=['EXT', 'AGR', 'CSN', 'OPN'])
    series = {'EXT':[sys.argv[1]], 'AGR':[sys.argv[2]], 'CSN':[sys.argv[3]], 'OPN':[sys.argv[4]]} 
    #input_data = pd.DataFrame(args, columns=['EXT', 'AGR', 'CSN', 'OPN'])
    input_data = pd.DataFrame(series)
    #print('arguments:', args)
    #print(input_data)

    #print(data)

    # create model
    X = data.drop('house', axis=1)
    y = data['house']
    X_train, X_valid, y_train, y_valid= train_test_split(X, y)
    model = DecisionTreeClassifier()
    model = model.fit(X_train, y_train)
    print('Training Score:  ', model.score(X_train, y_train))
    print('Validation Score:', model.score(X_valid, y_valid), '\n')

    # test model
    prediction = model.predict(input_data)
    print('Arguments:        [Extraversion, Agreeableness, Conscientiousness, Openness]')
    print('Feature Weights: ', model.feature_importances_, '\n')
    print('Prediction:      ', prediction[0])

if __name__ == '__main__':
    main()
