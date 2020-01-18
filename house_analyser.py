import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    houses = pd.read_csv('Data/scores_sorted.csv', usecols=[4])
    # Classify different hatstalls as just hatstalls
    houses = houses.replace(r'Hatstall.+', 'Hatstall', regex=True)

    # Count the number of times each house is chosen
    count_houses = houses['house'].value_counts()
    #print(count_houses)
    
    # Plot pie chart
    plt.style.use('seaborn')
    plt.figure(figsize=(8,4))
    plt.pie(count_houses, labels=count_houses.index, autopct='%1.1f%%', colors=['royalblue', 'gold', 'forestgreen', 'grey', 'firebrick'])
    plt.savefig('Graphs/houses_pie_chart')
    #plt.show()


if __name__ == '__main__':
    main()
