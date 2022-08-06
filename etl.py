from email.mime import base


############------------ IMPORTS ------------##################################
import csv


############------------ FUNCTION(S) ------------##############################
def read_csvs(path_to_csv):
    with open(path_to_csv, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in datareader:
            print(', '.join(row))
    

############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    pass