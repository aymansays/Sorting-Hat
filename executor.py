import cleaner
import analyser
import house_sorter
import house_analyser
import model

if __name__ == '__main__':
    print("Running tasks, this may take some time\n")
    cleaner.main()
    print("Finished cleaning\t | created Data/bigfive-3.csv (cleaner.py)")
    analyser.main()
    print("Analysed cleaned data\t | created plots in Graphs/ and ./posthoc.txt (analyser.py)")
    house_sorter.main()
    print("Done sorting the wizards | created Data/sorted_scores.csv (house_sorter.py)")
    house_analyser.main()
    print("Analysed all the houses\t | created Graphs/houses_pie_chart.png (house_analyser.py)")
    model.main()

    print("\nAll tasks complete")
