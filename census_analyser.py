import pandas as pd
from census_analyser_exceptions import *


class CensusAnalyser:
    def __init__(self, file_path):
        try:
            # reading csv file
            self.state_data_csv = pd.read_csv(file_path)
        except IOError:
            check_exceptions_type(file_path)

    def sort_in_alphabetical_order(self):
        sorted_data = self.state_data_csv.sort_values('State')
        sorted_data.to_json(
            r'C:\Users\FATHIMA\PycharmProjects\Census-Analyser\sorted_json_files\stateCensusSorted.json')
        return sorted_data


class CSVStateCensus(CensusAnalyser):
    # getting number of records
    def get_number_of_records_and_sort(self):
        number_of_records = self.state_data_csv.last_valid_index()
        self.sort_in_alphabetical_order()
        return number_of_records + 1


class CSVStateCode(CensusAnalyser):
    # getting number of records
    def get_number_of_records_and_sort(self):
        number_of_records = self.state_data_csv.last_valid_index()
        self.sort_in_alphabetical_order()
        return number_of_records + 1
