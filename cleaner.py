import sys
import numpy as np
import pandas as pd

columns = ['EXT1','EXT2','EXT3','EXT4','EXT5','EXT6','EXT7','EXT8','EXT9','EXT10',
           'AGR1','AGR2','AGR3','AGR4','AGR5','AGR6','AGR7','AGR8','AGR9','AGR10',
           'CSN1','CSN2','CSN3','CSN4','CSN5','CSN6','CSN7','CSN8','CSN9','CSN10',
           'OPN1','OPN2','OPN3','OPN4','OPN5','OPN6','OPN7','OPN8','OPN9','OPN10']

s_usecols = np.concatenate((np.arange(7,17), np.arange(27,57)))
b_usecols = np.concatenate((np.arange(0,10), np.arange(20,50), [106]))

def main():
    smallfive = pd.read_csv('Data/bigfive-1.csv', sep='\t', usecols=s_usecols, names=columns, header=0)
    bigfive = pd.read_csv('Data/bigfive-2.csv', sep='\t', usecols=b_usecols).dropna()
    
    # IPC is the number of records from a user's IP address
    # values >1 indicate multiple submissions or the IP is in a shared network
    bigfive = bigfive[bigfive['IPC'] == 1].drop(columns=['IPC'])

    # Join both datasets
    allfive = pd.concat([smallfive, bigfive], axis=0, ignore_index=True)
    
    # Remove responses that have missed a question (0=missed)
    allfive = allfive[~allfive.eq(0).any(1)] 
    # Remove responses with all the same numbers (Eg: all 1s)
    allfive = allfive[(allfive!=1).any(1) & (allfive!=2).any(1) & (allfive!=3).any(1) & (allfive!=4).any(1) & (allfive!=5).any(1)]
    
    allfive.to_csv('Data/bigfive-3.csv', index=False)


if __name__ == '__main__':
    main()
