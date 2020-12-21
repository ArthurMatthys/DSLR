import os
import sys
import itertools
import seaborn as sns
from matplotlib import pyplot as plt
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib

def scatterplot_df(df):
    """
    Function that prints a pairplot
    Values are colored by house categories
    """
    sns.pairplot(df, hue='Hogwarts House')
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
    scatterplot_df(df)
    
if __name__ == "__main__":
    main()
