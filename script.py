############------------ IMPORTS ------------##################################
import csv
import os

############------------ FUNCTION(S) ------------##############################
def read_csvs(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")
    return csvfile
    

def print_headers(data):
    '''
     print out how many columns a csv file has
     and their names
    '''
    for row in data:
        headers = ", ".join(row)
        print(f"\nFile has {len(headers)} columns.")
        
        print("\nHere's a list of its headers:")
        for header in headers.split(","):
            print(f" - {header}")
        
        return


def check_if_utf8_encoded(path_to_csv):
    # print(f"\nFile's encoding: {csvfile.encoding}")
    command = f"isutf8 {path_to_csv}"
    execute = os.system(command)

    if execute:
        print("\nFile not UTF8-encoded.\n")
        print(f"Error: {execute}")
    else:
        print("File is UTF8-encoded.")


def consume_csv_data(path_to_csv):
    '''
     print each row within a csv
    '''
    csvfile = read_csvs(path_to_csv)
    
    check_if_utf8_encoded(path_to_csv)
    
    data = csv.reader(
        csvfile,
        delimiter=" ",
        quotechar="|"
    )
    
    print_headers(data)


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    # path_to_csv = "constructorss.csv"
    path_to_csv = "example.csv"
    consume_csv_data(path_to_csv)