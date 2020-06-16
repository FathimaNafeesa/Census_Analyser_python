import csv
from census_analyser_exceptions import *
import pandas as pd


class CensusAnalyser:
    def __init__(self, file_path):
        try:
            # reading csv file
            self.state_data_csv = pd.read_csv(file_path)
        except FileNotFoundError as exception:
            raise FileNotCorrectError


class CSVStateCensus(CensusAnalyser):
    # getting number of records
    def get_number_of_records(self):
        number_of_records = self.state_data_csv.last_valid_index()
        return number_of_records+1



class CSVStateCode(CensusAnalyser):
    # getting number of records
    def get_number_of_records(self):
        number_of_records = self.state_data_csv.last_valid_index()
        return number_of_records + 1

    def


if __name__ == '__main__':
    csv_read = CSVStateCensus('CSV files/StateCensusData.csv')
    csv_read.get_number_of_records()
