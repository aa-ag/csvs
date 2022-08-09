############------------ IMPORTS ------------##################################
### relative
from django.shortcuts import render
from django.http import HttpResponseRedirect

### external
import csv
import random
import io
import chardet

############------------ FUNCTION(S) ------------##############################
def home(request):
    return render(request, 'checks/index.html')


def report(request):
    if request.method == 'POST':
        
        uploaded_file = request.FILES['file']
        
        in_memory_file = uploaded_file.read()

        isutf8_encoded = is_utf8_encoded(in_memory_file)

        if isutf8_encoded == "Yes":
            
            in_memory_file = in_memory_file.decode('utf-8')
            
            reader = generate_reader_from_file(in_memory_file)

            counts = count_columns_and_rows(reader)

            context = {
                "isutf8_encoded": isutf8_encoded,
                "columns": counts["columns"],
                "rows": counts["rows"],
                # "headers": "headers",
                # "sample": "sample"
            }
        else:
            encoding = detect_encoding(in_memory_file)

            context = {
                "isutf8_encoded": isutf8_encoded,
                "encoding": encoding,
            }
        return render(
            request, 
            'checks/report.html', 
            context=context
        )


def is_utf8_encoded(f):
    try:
        f.decode('utf-8')
        return "Yes"
    except:
        return "No"


def generate_reader_from_file(in_memory_file):
    reader = csv.reader(
        io.StringIO(in_memory_file),
        delimiter=" ",
        quotechar="|"
    )

    return reader


def detect_encoding(reader):
    match = chardet.detect(reader)
    return match["encoding"]



def count_columns_and_rows(data):
    
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


def list_headers(f):
    headers = dict(list(f)[0]).keys()
    return list(headers)



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