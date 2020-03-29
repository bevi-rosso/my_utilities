# exceltab_to_csv.py
# Python 3
# python exceltab_to_csv_py3.py /Users/aegan/Documents/Palantir\ CREDO_Out_576_8_30_2019_10_8_52.xlsx /Users/aegan/Documents/RE/

'''This python script is to extract each sheet in an Excel workbook as a new csv file'''

import csv
import xlrd
import sys

def ExceltoCSV(excel_file, csv_file_base_path):
    # today = input('Enter today like YYYY-MM-DD: ')
    workbook = xlrd.open_workbook(excel_file)

    for sheet_name in workbook.sheet_names():
        print('processing - ' + sheet_name)
        worksheet = workbook.sheet_by_name(sheet_name)
        csv_file_full_path = csv_file_base_path + sheet_name.lower().replace(" - ", "_").replace(" ","_") + '.csv'
        # csv_file_full_path = csv_file_base_path + today + sheet_name.lower().replace(" - ", "_").replace(" ","_") + '.csv'
        # csvfile = open(csv_file_full_path, 'w', encoding='utf8')
        csvfile = open(csv_file_full_path, 'wb')
        writetocsv = csv.writer(csvfile, quoting = csv.QUOTE_ALL)

        for rownum in range(worksheet.nrows):
            writetocsv.writerow(worksheet.row_values(rownum))

        csvfile.close()
        print(sheet_name + ' has been saved at - ' + csv_file_full_path)

if __name__ == '__main__':
    ExceltoCSV(excel_file = sys.argv[1], csv_file_base_path = sys.argv[2])