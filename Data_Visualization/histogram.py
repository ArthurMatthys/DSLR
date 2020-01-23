import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib


def main():
    """
    Main function
    """
    names = [('Hogwarts House', 2), ('Arithmancy', 1), ('Astronomy', 1),
             ('Herbology', 1), ('Defense Against the Dark Arts', 1),
             ('Divination', 1), ('Muggle Studies', 1), ('Ancient Runes', 1),
             ('History of Magic', 1), ('Transfiguration', 1), ('Potions', 1),
             ('Care of Magical Creatures', 1), ('Charms', 1), ('Flying', 1)]

    hogwarts_house = ["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"]
    args = lib.get_args()
    data = lib.open_data(args.data)
    data = [e.split(',') for e in data.split('\n')][:-1]
    column_type = lib.find_column(data[0], names)
    dic = {"Hufflepuff": [], "Gryffindor": [],
           "Slytherin": [], "Ravenclaw": []}
    name = column_type.index(2)
    for line in data[1:]:
        dic[line[name]].append(line)

    header = []
    for i, name in enumerate(data[0]):
        if column_type[i] == 1:
            header.append([name])
    print(header)
    all_data = []
    for house in hogwarts_house:
        actual_data = dic[house]
        new_format = header
        index = 0
        for _, line in enumerate(actual_data):
            for i, feature in enumerate(line):
                if column_type[i] == 1:
                    new_format[index].append(float(feature))
                    index += 1


if __name__ == "__main__":
    main()
