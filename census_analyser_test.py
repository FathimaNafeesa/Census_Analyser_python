import unittest

from census_analyser import *


class CensusAnalyserTest(unittest.TestCase):

    # for state census data
    def test_given_number_of_records_matches_the_returned_number_of_records_state_census_data(self):
        csv_read = CSVStateCensus('C:/Users/FATHIMA/PycharmProjects/Census-Analyser/CSV_files/StateCensusData.csv')
        result = csv_read.get_number_of_records_and_sort()
        assert result == 29

    # for state code data
    def test_given_number_of_records_matches_the_returned_number_of_records_state_code(self):
        csv_read = CSVStateCode('CSV_files/StateCode.csv')
        result = csv_read.get_number_of_records_and_sort()
        assert result == 37



if __name__ == '__main__':
    unittest.main()
