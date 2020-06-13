import csv


class CensusAnalyser:
    def __init__(self, file_name, rows=[]):
        # reading csv file
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            fields = next(csv_reader)
            for row in csv_reader:
                rows.append(row)
        self.total_records = csv_reader.line_num


class CSVStateCensus(CensusAnalyser):
    # getting number of records
    def get_number_of_records(self):
        number_of_records = self.total_records
        print(number_of_records)


OBJ = CSVStateCensus('CSV files/StateCensusData.csv')
OBJ.get_number_of_records()
