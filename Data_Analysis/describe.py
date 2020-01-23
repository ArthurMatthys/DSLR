import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib


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
    names = [('Arithmancy', 1), ('Astronomy', 1),
             ('Herbology', 1), ('Defense Against the Dark Arts', 1),
             ('Divination', 1), ('Muggle Studies', 1), ('Ancient Runes', 1),
             ('History of Magic', 1), ('Transfiguration', 1), ('Potions', 1),
             ('Care of Magical Creatures', 1), ('Charms', 1), ('Flying', 1)]

    args = lib.get_args()
    data = lib.open_data(args.data)
    data = [e.split(',') for e in data.split('\n')][:-1]
    column_type = lib.find_column(data[0], names)
    formated_data = []
    for j in range(len(data[0])):
        if column_type[j] == 0:
            continue
        new_lst = []
        for i in range(1, len(data)):
            if data[i][j] == "":
                continue
            if column_type[j] == 1:
                new_lst.append(float(data[i][j]))
            elif column_type[j] == 2:
                new_lst.append(data[i][j])
        formated_data.append([data[0][j], new_lst])
    to_print = []
    for column in formated_data:
        to_print.append([column[0]] + lib.describe(column))
    print_description(to_print)


if __name__ == "__main__":
    main()
