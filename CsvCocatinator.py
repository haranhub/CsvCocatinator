import os
import sys


def add_csv_to_csv(csv_main, csv_to_add, is_first):
    """
    adding the given csv_to_add file at the end of csv_main file
    :param csv_main: adding to this csv
    :param csv_to_add: this csv that need to be added
    :param is_first: a flag representation that says if csv_to_add is the first one so header should
                     be taken
    :return: None
    """

    fout = open(csv_main, "a")
    fin = open(csv_to_add)
    m = fin.readlines()

    start_from = 0
    if not is_first:
        start_from = 1

    for line in m[start_from:]:
        fout.write(line)
    # now the rest:
    fin.close()  # not really needed
    fout.close()


def main():
    """
    cocatinate all csv files in the current directory into "all_data.csv" file
    """


    path = os.path.realpath(os.curdir)
    csv_files_list = [f for f in os.listdir(path) if f.endswith('.csv') and not f.endswith('all_data.csv')]

    all_data = open("all_data.csv", 'a')
    all_data.close()
    is_first_flag = True

    for file_to_add in csv_files_list:
        print("adding \"" + file_to_add, end='')
        sys.stdout.flush()
        add_csv_to_csv("all_data.csv", file_to_add, is_first_flag)
        print(" ---------------> Done.")
        is_first_flag = False

    print("\nAll Done!")


if __name__ == "__main__":
    main()
