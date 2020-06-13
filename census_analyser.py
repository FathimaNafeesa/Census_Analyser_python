import csv
from census_analyser_exceptions import *


class CensusAnalyser:
    def __init__(self, file_name, rows=[]):
        try:
            # reading csv file
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                fields = next(csv_reader)
                for row in csv_reader:
                    rows.append(row)
            self.total_records = csv_reader.line_num
        except FileNotFoundError as exception:
            raise FileNotCorrectError


class CSVStateCensus(CensusAnalyser):
    # getting number of records
    def get_number_of_records(self):
        number_of_records = self.total_records
        print(number_of_records)


if __name__ == '__main__':
    csv_read = CSVStateCensus('CSV files/StateCensusData.csv')
    csv_read.get_number_of_records()
