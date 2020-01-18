# Harry Potter Sorting Hat
An analysis on the Big Five personality test in relation to Harry Potter houses.

## Libraries
 - pandas v0.25.2
 - numpy v1.17.2
 - matplotlib v3.0.3
 - scipy v1.3.1
 - sklearn v0.21.3

## Commands and Expected Output
The main command to run is `python executor.py` which runs all scripts in the correct order and outputs:
<br/>
```
Running tasks, this may take some time

Finished cleaning        | created Data/bigfive-3.csv (cleaner.py)
Analysed cleaned data    | created plots in Graphs/ and ./posthoc.txt (analyser.py)
Done sorting the wizards | created Data/sorted_scores.csv (house_sorter.py)
Analysed all the houses  | created Graphs/houses_pie_chart.png (house_analyser.py)
Trained the model        | model scores using DecisionTreeClassifier shown below (model.py)
Training Score:         1.0
Validation Score:       0.999

Feature Weights:
  * Extraversion:       0.185
  * Agreeableness:      0.261
  * Conscientiousness:  0.254
  * Openness:           0.3

All tasks complete
```
<br/>
If you would like to run the scripts yourself, then the ordering should be:

|  #  | Script | Description |
|  -  | ------ | ------ |
|  1. | cleaner.py | Cleans and combines bigfive-1.csv and bigfive-2.csv to create bigfive-3.csv in the Data folder. |
|  2. | analyser.py | Creates all the histograms and boxplot in Graphs folder.<br/>Also creates a posthoc.txt next to the scripts and a scores.csv in the Data folder that saves every row's scaled scores. |
|  3. | house\_sorter.py | Decides what house each response belongs based on the highest score or call a hatstall.<br/>Creates sorted\_scores.csv in the Data folder. |
|  4. | house_analyser.py | Creates a pie chart showing the percentage of responses atributing to what house they belonged to in Graphs folder. |
|  5. | model.py | Trains a model that predicts which house a response belongs to based the personality scores.<br/>Also outputs the training & validation scores and the feature wieghts to each personality to the terminal. |

These scripts do not rely on any arguments so you may run them as is. Eg: `python analyser.py`
