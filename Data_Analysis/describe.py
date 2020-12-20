import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib
from pandas import read_csv, merge, set_option
import numpy as np


def print_description(feature):
    """
    Format the output
    """
    features = ["", "Count", "Mean", "Std", "Min", "25%", "50%",
                "75%", "Max"]
    size = []
    for j, _ in enumerate(feature):
        size.append(len(feature[j][0]))

    for index, _ in enumerate(features):
        print(f"{features[index]:{10}}", end="")
        for j, _ in enumerate(feature):
            print(f"{str(feature[j][index]):{size[j] + 5}.{size[j] + 2}}",
                  end="")
        print("")

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
    df = df.drop(columns=["Index","Hogwarts House","First Name","Last Name","Birthday","Best Hand"])
    df = df.dropna().astype(float)

    to_print = []
    for (columnName, columnData) in df.iteritems():
        to_print.append([columnName] + lib.describe(columnData))
    print_description(to_print)


if __name__ == "__main__":
    main()
