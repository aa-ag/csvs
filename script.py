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


def consume_csv_data(path_to_csv):
    '''
     print each row within a csv
    '''
    data = read_csvs(path_to_csv)
    print_headers(data)


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    path_to_csv = "constructors.csv"
    consume_csv_data(path_to_csv)