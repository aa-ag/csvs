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
    '''
     execute linux command `isutf8` 
     from the `moreutils` module
    '''
    utf8_check_command = f"isutf8 {path_to_csv}"
    execute = os.system(utf8_check_command)

    if execute:
        print("\n⛔ File not UTF8-encoded.\n")
        print("This file's encoding:")
        os.system(f"uchardet {path_to_csv}")
        return False
    return True


def break_down_csv(data):
    '''
     count number of columns and rows,
     and make both numbers human-readable
    '''
    column_count = 0
    row_count = 0
    
    for row in data:
        if column_count == 0:
            headers = ", ".join(row)
            column_count = len(headers)
            row_count += 1
        else:
            row_count += 1
    
    column_count = "{:,}".format(column_count)
    row_count = "{:,}".format(row_count - 1)

    return column_count, row_count, headers


def get_headers(headers):
    '''
     print out how many columns a csv file has
     and their names
    '''
    for header in headers.split(','):
        print(header)


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
        print("\n✅ File is UTF8-encoded.\n")

        data = csv.reader(
            csvfile,
            delimiter=" ",
            quotechar="|"
        )
        
        parts = break_down_csv(data)
        print(f"File has {parts[0]} columns.👉")
        print(f"👇 And {parts[1]} rows.")
        
        print("\nHere's a list of its headers:")
        print(f"👆 {parts[2]}")
        
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    # path_to_csv = "constructors.csv"
    path_to_csv = "example.csv"
    analyse_csv(path_to_csv)