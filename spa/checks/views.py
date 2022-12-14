############------------ IMPORTS ------------##################################
### relative
from asyncore import read
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

### external
import csv
import io
import chardet
import random
from time import sleep
import os
import datetime

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
    if request.method == "POST":
        
        uploaded_file = request.FILES["file"]
        
        in_memory_file = uploaded_file.read()

        uploaded_file_name = uploaded_file.name.replace(".csv", "")
        uploaded_file_name = uploaded_file_name.replace(".", "")
        uploaded_file_name = uploaded_file_name.replace("-", "")
        uploaded_file_name = uploaded_file_name.replace(" ", "_")

        isutf8_encoded = is_utf8_encoded(in_memory_file)

        if isutf8_encoded == "Yes":
            
            in_memory_file = in_memory_file.decode("utf-8")
            
            reader = generate_reader_from_file(in_memory_file)
            
            metadata = extract_csv_metadata(reader)
            
            dictreader = generate_dictreader_from_file(in_memory_file)
            
            data_checks = perform_data_checks(dictreader, metadata["headers"])
            
            # sample_file_name = f"{uploaded_file_name}_sample.csv"

            is_ok = False

            if isutf8_encoded == "Yes" and \
                data_checks["names_are_valid"] == "Yes" and \
                    data_checks["mandatory_headers_are_in"] == "Yes":
                    is_ok = True

            context = {
                "isutf8_encoded": isutf8_encoded,
                "columns": metadata["columns"],
                "rows": metadata["rows"],
                "headers": metadata["headers"],
                "uploaded_file_name": uploaded_file,
                "names_are_valid": data_checks["names_are_valid"],
                "dates_are_valid": data_checks["dates_are_valid"],
                "mandatory_headers_are_in": data_checks["mandatory_headers_are_in"],
                "is_ok": is_ok,
            }

        else:
            encoding = detect_encoding(in_memory_file)

            context = {
                "isutf8_encoded": isutf8_encoded,
                "encoding": encoding,
            }

        return render(
            request, 
            "checks/report.html", 
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

def generate_dictreader_from_file(in_memory_file):
    '''
     consume a CSV file and generate/return a 
     csv.reader object with it
    '''
    reader = csv.DictReader(
        io.StringIO(in_memory_file),
        delimiter=",",
        quotechar="|"
    )
    return reader


def generate_reader_from_file(in_memory_file):
    '''
     consume a CSV file and generate/return a 
     csv.reader object with it
    '''
    reader = csv.reader(
        io.StringIO(in_memory_file),
        delimiter=",",
        quotechar="|"
    )
    return reader


def detect_encoding(reader):
    '''
     consume a csv.reader object and 
     detect/return its encoding
    '''
    match = chardet.detect(reader)
    return match["encoding"]


def extract_csv_metadata(data):
    '''
     consume a css.reader and
     (i) count its columns,
     (ii) generate/return a list of its headers,
     (iii) count its rows,
    '''
    headers = 0
    column_count = 0
    row_count = 0
    
    for row in data:
        if column_count == 0:
            columns = row
            headers = ", ".join(columns)
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


def generate_random_numbers_list(row_count):
    '''
     convert row_count into an integer, 
     and generate a list of random numbers from 
     1 to number of rows for each csv file.
    '''
    row_count = row_count.replace(",", "")

    
    random_list = random.sample(
        range(1, int(row_count)),
        25
    )
    return random_list


def make_sample(file_name, reader, random_numbers):
    '''
     create a csv file and save it to static
     saving headers from original csv, and 
     25 randomly selected rows (to sample original data)
    '''
    with open(
        f"static/samples/{file_name}_sample.csv",
        "w",
        newline=""
    ) as csv_file:

        csv_writter = csv.writer(
            csv_file,
            delimiter=",",
            quotechar="|"
        )
        
        for i, row in enumerate(reader):
            if i == 0 or i in (random_numbers):
                csv_writter.writerow(row)
            

def delete_sample(sample_file_name):
    sleep(5)
    samples_directory = "static/samples/"
    os.remove(os.path.join(samples_directory, sample_file_name))


def perform_data_checks(dictreader, headers):
    mandatory_headers_are_in = "No"
    names_are_valid = "Yes"
    dates_are_valid = "Yes"

    if "name" in headers.split(", "):
        mandatory_headers_are_in = "Yes"

        for row in dictreader:
            if row["name"] == None:
                names_are_valid = "No"
            
            try:
                datetime.datetime.strptime( row["date"].strip('"'), '%Y-%m-%d')
            except:
                dates_are_valid = "No"
    else:
        names_are_valid = "No"

    data_checks_response = {
        "mandatory_headers_are_in": mandatory_headers_are_in,
        "names_are_valid": names_are_valid,
        "dates_are_valid": dates_are_valid
    }

    return data_checks_response