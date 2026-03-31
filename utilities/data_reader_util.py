import json
import csv
import openpyxl


def read_json_file(filepath):
    data =[]
    try:
        file = open(filepath, "r")
        json_data = json.load(file)
        for record in json_data:
            data.append(list(record.values()))
    except Exception as e:
        print(f"Error while loading json file : {e}")
    return data

def read_csv_file(filepath):
    data = []
    try:
        file = open(filepath, newline='', encoding='utf-8')
        reader = csv.DictReader(file)
        for row in reader:
            data.append(list(row.values()))
    except Exception as e:
        print(f"Error while reading data from csv : {e}")
    return data

def read_excel_file(filepath, sheet_name):
    data = []
    try:
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook[sheet_name] if sheet_name else workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)
    except Exception as e:
        print(f"Error while loading excel file : {e}")
    return data
