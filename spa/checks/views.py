############------------ IMPORTS ------------##################################
from django.shortcuts import render
from django.template import loader
import csv
import random
import os

############------------ FUNCTION(S) ------------##############################
def home(request):
    return render(request, 'checks/index.html')


def generate_reader_object(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")
    return csvfile


def read_data_from_reader_object(csv_reader_object):
    '''
     execute csv's reader function to "read" the data 
     from the passed file
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

    counts = {
        "columns": column_count,
        "rows": row_count
    }

    return counts


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

    isutf8 = check_if_utf8_encoded(path_to_csv)

    if isutf8:
        print("\n✅ File is UTF8-encoded.\n")
        
        counts = count_columns_and_rows(csv_reader_object)
        print(f"👉 File has {counts['columns']} columns.")
        print(f"And {counts['rows']} rows.👇")


        headers_list = list_headers(path_to_csv)
        print("\nHere's a list of its headers:")
        print(f"👆{headers_list}")
    
        return True
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return False


def make_sample(path_to_csv, sample_size, sample_indexes):
    '''
     open and read a csv file, 
     and make a sample csv that gets either 
     (i) a specific set of indexes/rows 
     or (ii) an N number of rows at random indexes
    '''
    with open(
            f"sample.csv", "w", newline=""
        ) as csvfile:

        csv_reader_object = generate_reader_object(path_to_csv)
        counts = count_columns_and_rows(csv_reader_object)
        row_count = int(counts['rows'].replace(',', ''))

        if sample_indexes:
            target = sample_indexes
        else:
            random_indexes = random.sample(
                range(1, row_count), 
                sample_size
            )

            target = random_indexes

        csv_reader_object = generate_reader_object(path_to_csv)
        data = read_data_from_reader_object(csv_reader_object)

        csv_writer = csv.writer(csvfile)
        
        for i, row in enumerate(data):
            if i in target:
                csv_writer.writerow(row)



############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    path_to_csv = "constructors.csv"
    # path_to_csv = "example.csv"

    analysis = analyse_csv(path_to_csv)
    
    sample_size = 25
    # sample_indexes = [11201, 1822, 9787, 9444, 5146, 9383, 9130, 11669, 7732, 8144, 435, 5467, 2178, 7099, 781, 12023, 8180, 3198, 238, 7466, 5073, 11742, 2153, 11062, 2689]
    sample_indexes = []


    if analysis:
        make_sample(path_to_csv, sample_size, sample_indexes)