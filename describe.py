from utils import *


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
    main()
