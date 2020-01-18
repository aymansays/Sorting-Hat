import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# Plot the histogram and line for a personality
def plot_scores(personality_score, i):
    fit = stats.norm.pdf(personality_score, personality_score.mean(), personality_score.std())

    plt.subplot(1, 4, i, title=personality_score.name)
    plt.xlabel('score')
    plt.plot(personality_score, fit, color='orangered')
    plt.hist(personality_score, density=True, color='deepskyblue', alpha=0.5)


# Plot all graphs
def create_graphs(scores):
    # Sort each column in ascending order
    # matplotlib runs faster if all columns are sorted
    sorted_scores = scores.apply(lambda p: p.sort_values().values)
    
    # Plot histograms
    plt.figure(figsize=(8,4))
    plt.hist(sorted_scores.values, density=True, alpha=0.80)
    plt.suptitle('Personality Probability Density')
    plt.xlabel('Score')
    plt.ylabel('Probability Density')
    plt.legend(sorted_scores.columns)
    plt.savefig('Graphs/probability_densities')
    
    # Plot histograms with a line seperately
    plt.figure(figsize=(20,4))
    sorted_scores.apply(lambda ps: plot_scores(ps, scores.columns.get_loc(ps.name)+1))
    plt.suptitle('Personality Probability Density')
    plt.savefig('Graphs/probability_densities_seperate')
   
    # Plot boxplots
    plt.figure(figsize=(8,5))
    sorted_scores.apply(lambda ps: plt.boxplot(ps, positions=[sorted_scores.columns.get_loc(ps.name)+1], notch=True, vert=False))
    plt.yticks(np.arange(len(sorted_scores.columns))+1, sorted_scores.columns)
    plt.suptitle('Personality Score Boxplot')
    plt.xlabel('Score')
    plt.ylabel('Personality')
    plt.savefig('Graphs/boxplots')
    #plt.show()


# Post Hoc analysis using Tukey's HSD
def statistics(scores):
    melted_scores = pd.melt(scores)
    posthoc = pairwise_tukeyhsd(melted_scores['value'], melted_scores['variable'], alpha=0.05)
    
    # Save post hoc results in a text file
    file = open('posthoc.txt', 'w')
    file.write(posthoc.summary().as_text())
    file.close()


def main():
    bigfive = pd.read_csv('Data/bigfive-3.csv')

    # Weight of each question according to the sourced data
    scale = np.tile((np.array([1,-2,3,-4,5,-1,2,-3,4,-5])), 4)
    scaledfive = bigfive + scale

    # Sum the score of the questions related to each personality
    scores = pd.concat([scaledfive.loc[:, 'EXT1':'EXT10'].sum(1),
                         scaledfive.loc[:, 'AGR1':'AGR10'].sum(1),
                         scaledfive.loc[:, 'CSN1':'CSN10'].sum(1),
                         scaledfive.loc[:, 'OPN1':'OPN10'].sum(1)],
                        axis=1)
    scores.columns = ['EXT', 'AGR', 'CSN', 'OPN']
    
    plt.style.use('seaborn')
    create_graphs(scores)
    statistics(scores)

    scores.to_csv('Data/scores.csv', index=False)


if __name__ == '__main__':
    main()
