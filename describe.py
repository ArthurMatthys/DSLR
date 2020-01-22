import argparse


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


def get_args():
    """
    Parse the input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str,
                        help="File containing the data to work on")
    return parser.parse_args()


def run():
    """
    Main function
    """
    args = get_args()
    data = open_data(args.data)
    data = [e.split(',') for e in data.split('\n')]
    print(find_column(data[0]))


if __name__ == "__main__":
    run()
