############------------ IMPORTS ------------##################################
### relative
from django.shortcuts import render
from django.http import HttpResponseRedirect

### external
import csv
import io
import chardet

############------------ VIEW(S) ------------##############################
def home(request):
    '''
     View for home-page rendering template `home.html`
     where end-user uploads a CSV file for analysis
    '''
    return render(request, 'checks/home.html', {})


def report(request):
    '''
     View to (i) redirect the end-user to a `report` page,
     and (ii) process an input CSV file and analyse it
    '''
    if request.method == 'POST':
        
        uploaded_file = request.FILES['file']
        
        in_memory_file = uploaded_file.read()

        isutf8_encoded = is_utf8_encoded(in_memory_file)

        if isutf8_encoded == "Yes":
            
            in_memory_file = in_memory_file.decode('utf-8')
            
            reader = generate_reader_from_file(in_memory_file)

            metadata = extract_csv_metadata(reader)

            context = {
                "isutf8_encoded": isutf8_encoded,
                "columns": metadata["columns"],
                "rows": metadata["rows"],
                "headers": metadata["headers"],
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


############------------ HELPER FUNCTION(S) ------------##############################
def is_utf8_encoded(in_memory_file):
    '''
     check if a file is UTF8-encoded
     by attempting to decode it as such,
     and return Yes/No
    '''
    try:
        in_memory_file.decode('utf-8')
        return "Yes"
    except:
        return "No"


def generate_reader_from_file(in_memory_file):
    '''
     consume a CSV file and generate a 
     csv.reader object with it
    '''
    reader = csv.reader(
        io.StringIO(in_memory_file),
        delimiter=" ",
        quotechar="|"
    )
    return reader


def detect_encoding(reader):
    match = chardet.detect(reader)
    return match["encoding"]


def extract_csv_metadata(data):
    headers = 0
    column_count = 0
    row_count = 0
    
    for row in data:
        if column_count == 0:
            columns = ", ".join(row)
            headers = columns
            column_count = len(columns)
            row_count += 1
        else:
            row_count += 1
    
    column_count = "{:,}".format(column_count)
    row_count = "{:,}".format(row_count - 1)

    metadata = {
        "columns": column_count,
        "rows": row_count,
        "headers": headers,
    }

    return metadata


def make_sample():
    '''
     https://docs.djangoproject.com/en/4.1/howto/outputting-csv/
    '''
    pass