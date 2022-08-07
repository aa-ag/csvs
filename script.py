############------------ IMPORTS ------------##################################
import csv
import os

############------------ FUNCTION(S) ------------##############################
def generate_reader_object(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")
    return csvfile


def read_data_from_reader_object(csv_reader_object):
    '''
     execute csv's reader function to "read" it
    '''
    data = csv.reader(
            csv_reader_object,
            delimiter=" ",
            quotechar="|"
        )
    return data


def check_if_utf8_encoded(path_to_csv):
    '''
     execute linux command `isutf8` 
     from the `moreutils` module to check if file is
     utf8 encoded, and if an error is raised
     execute `uchardet` to detect encoding
    '''
    utf8_check_command = f"isutf8 {path_to_csv}"
    execute = os.system(utf8_check_command)

    if execute:
        print("\n⛔ File not UTF8-encoded.\n")
        print("This file's encoding:")
        os.system(f"uchardet {path_to_csv}")
        return False
    return True


def count_columns_and_rows(csv_reader_object):
    '''
     count number of columns and rows,
     and make both numbers human-readable
    '''

    data = read_data_from_reader_object(
        csv_reader_object
    )
    
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


def list_headers(path_to_csv):
    '''
     open the csv from its path and
     return it's headers 
     (first column's keys in a DictRead object)
    '''
    with open(path_to_csv) as csv_file:
        dict_reader = csv.DictReader(csv_file)

        headers = dict(list(dict_reader)[0]).keys()
        return list(headers)


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

    csv_reader_object = generate_reader_object(path_to_csv)

    parts = count_columns_and_rows(csv_reader_object)
    print(f"File has {parts[0]} columns.👉")
    print(f"👇 And {parts[1]} rows.")


    headers = list_headers(path_to_csv)
    print("\nHere's a list of its headers:")
    print(f"👆 {headers}")

    # isutf8 = check_if_utf8_encoded(path_to_csv)

    # if isutf8:
    #     print("\n✅ File is UTF8-encoded.\n")
        
    #     parts = break_down_csv(data)
    #     print(f"File has {parts[0]} columns.👉")
    #     print(f"👇 And {parts[1]} rows.")
        
    #     print("\nHere's a list of its headers:")
    #     print(f"👆 {parts[2]}")
        
    #     print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     return True
    # else:
    #     print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     return False


def make_sample(path_to_csv):
    pass


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    path_to_csv = "constructors.csv"
    # path_to_csv = "example.csv"

    analysis = analyse_csv(path_to_csv)
    
    if analysis:
        make_sample(path_to_csv)