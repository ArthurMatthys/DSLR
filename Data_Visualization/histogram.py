import os
import sys
from matplotlib import pyplot

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib

def sephist(col):


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
    hogwarts_house = ["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"]

    args = lib.get_args()
    df = lib.open_data(args.data, names)[1:]
    df = df.drop(columns=["Index","First Name","Last Name","Birthday","Best Hand"])
    df = df.dropna()
    cols = df.columns
    df[cols[1:]] = df[cols[1:]].astype(float)

    list_colnames = list(cols)[1:]
    for 

    # print(list_colnames)   
    # print(df) 
    # for name in list_colnames:
    #     subset = df[name].hist(by=df['Hogwarts House'])
    #     for axis in subset.flatten():
    #         axis.set_xticklabels([])
    #         axis.set_yticklabels([])
    # pyplot.show()

if __name__ == "__main__":
    main()
