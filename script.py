############------------ IMPORTS ------------##################################
import csv
from email import header
from itertools import count
import os

############------------ FUNCTION(S) ------------##############################
def read_csvs(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")
    return csvfile


def check_if_utf8_encoded(path_to_csv):
    command = f"isutf8 {path_to_csv}"
    execute = os.system(command)

    if execute:
        return False
    return True


def get_row_and_column_count(data):
    column_count = 0
    row_count = 0
    
    for row in data:
        if column_count == 0:
            columns = ", ".join(row)
            column_count = len(columns)
            row_count += 1
        else:
            row_count += 1
    
    column_count = "{:,}".format(column_count)
    row_count = "{:,}".format(row_count - 1)

    return column_count, row_count


def get_headers(data):
    '''
     print out how many columns a csv file has
     and their names
    '''
    for row in data:
        print(row)


def analyse_csv(path_to_csv):
    '''
     read a csv file using it's path,
     and call helper functions to check:
       - if the csv is utf8 encoded,
       - what its headers are,
       - how many columns it has,
       - its row count
    '''
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    csvfile = read_csvs(path_to_csv)
    
    isutf8 = check_if_utf8_encoded(path_to_csv)
    
    if isutf8:
        print("\nFile is UTF8-encoded.\n")

        data = csv.reader(
            csvfile,
            delimiter=" ",
            quotechar="|"
        )
        
        counts = get_row_and_column_count(data)
        print(f"File has {counts[0]} columns.")
        print(f"And {counts[1]} rows.")
        
        headers = get_headers(data)
        print("\nHere's a list of its headers:")
        print(headers)
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("\nFile not UTF8-encoded.\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    path_to_csv = "constructors.csv"
    # path_to_csv = "example.csv"
    analyse_csv(path_to_csv)