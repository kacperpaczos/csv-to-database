import logging
import sys
import os
import mysql.connector
logging.basicConfig(level=logging.CRITICAL)


if __name__ == '__main__':
    for i in range(0, len(sys.argv)):
        if "--" in sys.argv[i]:
            path = sys.argv[i]
            path = path[2:]

    if os.path.isdir(path):
        print("SELECTED DIRECTORY: '" + path + "'")
    elif os.path.isfile(path):
        print("SELECTED FILE: '" + path + "'")
    else:
        sys.exit("PATH ERROR")

    print()
    """
    file_content = []
    macierzWyplat = []
    with open(file) as my_file:
        for line in my_file:
            file_content.append(line)

    x=file_content[0]
    logging.info('Ilośc wierszy ' + x)
    y=file_content[1]
    logging.info('Ilosc kolumn ' + y)
    """

