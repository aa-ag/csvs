from email.mime import base


############------------ IMPORTS ------------##################################
import csv


############------------ FUNCTION(S) ------------##############################
def read_csvs(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")
    data = csv.reader(csvfile, delimiter=" ", quotechar="|")

    return data


def consume_csv_data():
    '''
     print each row within a csv
    '''
    path_to_csv = "constructors.csv"
    
    data = read_csvs(path_to_csv)
    print_headers(data)
    

def print_headers(data):
    for row in data:
        headers = ", ".join(row)
        print(f"\nThere are {len(headers)} columns on this file.")
        print("\nHere's a list of all headers:")
        print(headers.split(","),"\n")
        return


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    consume_csv_data()