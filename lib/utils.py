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
        if element == elem[0]:
            return elem[1]
    return 0


def find_column(column_names, names):
    """
    Get the index of column we need to work on
    """

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
    return [length, mean, std, minimun, first_quartile, median,
            third_quartile, maximum]
