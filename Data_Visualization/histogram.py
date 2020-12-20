import os
import sys
from matplotlib import pyplot as plt

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib

def plot_df(df, names, list_colnames):
    """
    Function that plots, for each course, the distribution of grades per house
    It overlays the results : each house is present on each field
    """
    colors = ["b", "r", "y", "g"]
    hogwarts_house = ["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"]

    plt.figure(figsize=(16,4))
    plt.suptitle('Distribution of grades per Houses for each class')
    for i, feature_name in enumerate(list_colnames, start=1):
        plt.subplot(4, 4, i)
        for j, house in enumerate(hogwarts_house):
            plt.hist(df.loc[df['Hogwarts House'] == house][feature_name], alpha=0.5, color=colors[j])
            plt.tick_params(axis='both', which='both', left=False, labelleft=False, bottom=False, labelbottom=False)
            plt.xlabel(feature_name)
    plt.legend(hogwarts_house, bbox_to_anchor=(5, 1))
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
    plot_df(df, names, list_colnames)
    

if __name__ == "__main__":
    main()
