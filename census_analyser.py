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

    def get_map_of_state_and_census_file(self, format):
        dictionary = self.state_data_csv.to_dict()
        json_file = self.state_data_csv.to_json()
        csv_file = self.state_data_csv.to_csv()

        def map(format=format):
            switcher = {
                0: dictionary,
                1: json_file,
                2: csv_file
            }
            return switcher.get(format, "nothing")

        print(map())


class CSVStateCensus(CensusAnalyser):
    # getting number of records
    def get_number_of_records_and_sort(self):
        number_of_records = self.state_data_csv.last_valid_index()
        return number_of_records + 1

    def sort_in_alphabetical_order(self):
        self.sort_in_alphabetical_order()


class CSVStateCode(CensusAnalyser):
    # getting number of records
    def get_number_of_records_and_sort(self):
        number_of_records = self.state_data_csv.last_valid_index()
        return number_of_records + 1

    def sort_in_alphabetical_order(self):
        self.sort_in_alphabetical_order()

    def get_map_of_state_and_census_data(self):
        print("Select the required format: \n 1.Dictionary \n 2.json \n 3.csv")
        format = input("Format required:")
        self.get_map_of_state_and_census_file(format)



