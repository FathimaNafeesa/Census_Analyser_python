import pandas as pd
from census_analyser_exceptions import *


class StateCensusAnalyser:
    def __init__(self, file_path):
        try:
            self.state_census_csv = pd.read_csv(file_path)
        except IOError:
            check_exceptions_type(file_path)


class StateCodeAnalyser:
    def __init__(self, file_path):
        try:
            self.state_census_csv = pd.read_csv(file_path)
        except IOError:
            check_exceptions_type(file_path)


class CSVHandler(StateCensusAnalyser, StateCensusAnalyser):

    @staticmethod
    def get_number_of_records(census_file):
        number_of_records = census_file.last_valid_index()
        return number_of_records + 1

    @staticmethod
    def sort_data_frame(census_file, column_name, order=True):
        sorted_data = census_file.sort_values(column_name, ascending=order)
        sorted_data.to_json(
            r'C:\Users\FATHIMA\PycharmProjects\Census-Analyser\sorted_json_files\stateCensusSorted.json')
        return sorted_data

    @staticmethod
    def get_map_of_state_and_census_file(self, format_of_file):
        dictionary = self.state_data_csv.to_dict()
        json_file = self.state_data_csv.to_json()
        csv_file = self.state_data_csv.to_csv()

        def get_map(format_of_file_=format_of_file):
            switcher = {
                0: dictionary,
                1: json_file,
                2: csv_file
            }
            return switcher[format_of_file_]

        print(get_map())


class _CensusAnalyser(CSVHandler):

    def get_number_of_records(self):
        self.get_number_of_records()

    def sort_in_alphabetical_order(self):
        self.sort_data_frame(self.state_census_csv, 'State')

    def get_map_of_state_and_census_data(self):
        print("Select the required format: \n 1.Dictionary \n 2.json \n 3.csv")
        format_of_file = int(input("Format required:"))
        self.get_map_of_state_and_census_file(format_of_file)

    def sort_according_to_population_density(self):
        self.sort_data_frame(self.state_census_csv, 'population')

    def sort_according_to_area(self):
        self.sort_data_frame(self.state_census_csv, 'Area', False)





