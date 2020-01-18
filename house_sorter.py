# model.py

# imports
import pandas as pd

# labels data with house based on survey answers
def house_sort(x):
    # count number of winners
    wins = []
    if (x.g_win == 'true'): wins.append('Gryffindor')
    if (x.r_win == 'true'): wins.append('Ravenclaw')
    if (x.s_win == 'true'): wins.append('Slytherin')
    if (x.h_win == 'true'): wins.append('Hufflepuff')
    #print(wins)
    # returns single winner, or hatstall for multiple winners
    if (len(wins) == 1): return wins[0]
    #elif len(wins) == 4: return '4 way tie'
    else: return 'Hatstall: ' + str(wins)


def main():
    # import CSV
    data = pd.read_csv('Data/scores.csv')

    # compute max column
    data['max_score'] = data.max(axis=1)

    # returns wins for each house
    data.loc[data['EXT'] == data['max_score'], 'g_win'] = 'true'
    data.loc[data['EXT'] != data['max_score'], 'g_win'] = 'false'
    data.loc[data['OPN'] == data['max_score'], 'r_win'] = 'true'
    data.loc[data['OPN'] != data['max_score'], 'r_win'] = 'false'
    data.loc[data['CSN'] == data['max_score'], 's_win'] = 'true'
    data.loc[data['CSN'] != data['max_score'], 's_win'] = 'false'
    data.loc[data['AGR'] == data['max_score'], 'h_win'] = 'true'
    data.loc[data['AGR'] != data['max_score'], 'h_win'] = 'false'

    # labels wins for each dataset
    data['house'] = data.apply(house_sort, axis=1)

    # formating
    data = data.drop(['max_score', 'g_win', 'r_win', 's_win', 'h_win'], axis=1)

    # Output
    #print(data)
    #test = data.loc[data['house'] == 'Hatstall']
    #test = data.loc[data['house'] == '4 way tie']
    #print(test)

    # write to csv
    data.to_csv('Data/scores_sorted.csv', index=False)

if __name__ == '__main__':
    main()
