# model.py
# Outputs the Training and Validation Scores
# To be used in the Executor.py

# imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier 	
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import sys

def main():
    # import CSV
    data = pd.read_csv('Data/scores_sorted.csv')

    # create model
    X = data.drop('house', axis=1)
    y = data['house']
    X_train, X_valid, y_train, y_valid= train_test_split(X, y)
    model = DecisionTreeClassifier()
    model = model.fit(X_train, y_train)

    # Output Scores
    print("Trained the model\t | model scores using DecisionTreeClassifier shown below (model.py)")
    print('Training Score:\t\t' + str(model.score(X_train, y_train)))
    print('Validation Score:\t' + str(round(model.score(X_valid, y_valid), 3)), '\n')

    print('Feature Weights:')
    print('  * Extraversion:\t' + str(round(model.feature_importances_[0], 3)))
    print('  * Agreeableness:\t' + str(round(model.feature_importances_[1], 3)))
    print('  * Conscientiousness:\t' + str(round(model.feature_importances_[2], 3)))
    print('  * Openness:\t\t' + str(round(model.feature_importances_[3], 3)))

    # test model
    #prediction = model.predict(input_data)
    #print('Arguments: [Extraversion, Agreeableness, Conscientiousness, Openness]')
    #print('Prediction:', prediction[0])

if __name__ == '__main__':
    main()
