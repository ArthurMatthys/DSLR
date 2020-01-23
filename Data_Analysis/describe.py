import argparse


def get_args():
    """
    Parse the input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str,
                        help="File containing the data to work on")
    return parser.parse_args()


def open_data(filename):
    """
    Open the given file
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError
    except IsADirectoryError:
        raise IsADirectoryError
    except PermissionError:
        raise PermissionError
    return content


def in_list(lst, element):
    """
    return 1 if element is in lst else 0
    """
    for elem in lst:
        if element == elem:
            return 1
    return 0


def find_column(column_names):
    """
    Get the index of column we need to work on
    """

    names = ['Arithmancy', 'Astronomy', 'Herbology',
             'Defense Against the Dark Arts', 'Divination',
             'Muggle Studies', 'Ancient Runes', 'History of Magic',
             'Transfiguration', 'Potions', 'Care of Magical Creatures',
             'Charms', 'Flying']

    list_index = [in_list(names, name) for name in column_names]
    return list_index


def standard_deviation(value, mean, length):
    """
    Evaluate the std of a list
    """
    variance = sum([(e - mean)**2 for e in value])
    return ((1/(length-1)) * variance)**(1/2)


def describe(column):
    """
    Evaluate all features for all columns
    """
    data = sorted(column[1])
    length = len(data)
    mean = format(sum(data) / length, '.4f')
    std = format(standard_deviation(data, float(mean), length), '.4f')
    minimun = format(data[0], '.4f')
    first_quartile = format(data[length//4], '.4f')
    median = format(data[length//2], '.4f')
    third_quartile = format(data[3 * length//4], '.4f')
    maximum = format(data[-1], '.4f')
    return [column[0], length, mean, std, minimun, first_quartile, median,
            third_quartile, maximum]


def print_description(feature):
    """
    Format the output
    """
    features = ["", "Count", "Mean", "Std", "Min", "25%", "50%",
                "75%", "Max"]
    size = []
    for j in range(len(feature)):
        size.append(len(feature[j][0]))

    for index in range(len(features)):
        print(f"{features[index]:{10}}", end="")
        for j in range(len(feature)):
            print(f"{str(feature[j][index]):{size[j] + 5}.{size[j] + 2}}",
                  end="")
        print("")

    return


def run():
    """
    Main function
    """
    args = get_args()
    data = open_data(args.data)
    data = [e.split(',') for e in data.split('\n')]
    column_type = find_column(data[0])
    formated_data = []
    for j in range(len(data[0])):
        if column_type[j] == 0:
            continue
        new_lst = []
        for i in range(1, len(data)-1):
            if data[i][j] == "":
                continue
            try:
                new_lst.append(float(data[i][j]))
            except ValueError:
                print(i, j, data[0][j], data[i][j])
                raise ValueError
        formated_data.append([data[0][j], new_lst])
    to_print = []
    for column in formated_data:
        to_print.append(describe(column))
    print_description(to_print)


if __name__ == "__main__":
    run()
