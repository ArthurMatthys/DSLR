import os
import sys
import itertools
from matplotlib import pyplot as plt
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib

def scatterplot_df(df, names, list_colnames):
    """
    Function that plots, for each course, a scatter.
    Each feature against another
    """

    plt.figure(figsize=(9,9))
    plt.suptitle('Scatterplot of features against one another')
    combinations = itertools.combinations(list_colnames, 2)
    for i, (f0,f1) in enumerate(combinations, start=1):
        plt.subplot(9, 9, i)
        plt.scatter(df[f0],df[f1])
        plt.tick_params(axis='both', which='both', left=False, labelleft=False, bottom=False, labelbottom=False)
        plt.xlabel(f1)
        plt.ylabel(f0)
    plt.show()

def main():
    """
    Main function
    """
    names = ["Index","Hogwarts House","First Name","Last Name","Birthday",
            "Best Hand","Arithmancy","Astronomy","Herbology",
            "Defense Against the Dark Arts","Divination",
            "Muggle Studies","Ancient Runes","History of Magic",
            "Transfiguration","Potions","Care of Magical Creatures",
            "Charms","Flying"]

    args = lib.get_args()
    df = lib.open_data(args.data, names)[1:]
    df = df.drop(columns=["Index","First Name","Last Name","Birthday","Best Hand"])
    df = df.dropna()
    cols = df.columns
    df[cols[1:]] = df[cols[1:]].astype(float)
    list_colnames = list(cols)[1:]
    scatterplot_df(df, names, list_colnames)
    

if __name__ == "__main__":
    main()
