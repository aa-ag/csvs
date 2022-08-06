############------------ IMPORTS ------------##################################
import csv


############------------ FUNCTION(S) ------------##############################
def read_csvs(path_to_csv):
    '''
     consume a path and open that file
    '''
    csvfile = open(path_to_csv, newline="")

    print(f"\nFile's encoding: {csvfile.encoding}")

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
    '''
     print out how many columns a csv file has
     and their names
    '''
    for row in data:
        headers = ", ".join(row)
        print(f"\nThere are {len(headers)} columns on this file.")
        
        print("\nHere's a list of all headers:")
        for header in headers.split(","):
            print(f" - {header}")
        
        return


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    consume_csv_data()