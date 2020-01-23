import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lib


def main():
    """
    Main function
    """
    to_print = lib.format_data()


if __name__ == "__main__":
    main()
