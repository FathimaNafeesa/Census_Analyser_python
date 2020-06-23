from dao_class_census_analyser import *
from dto_class_census import *


class CensusAdapter:
    @staticmethod
    def get_dao_data_frame(dto, data_frame=None):
        if data_frame is None:
            return None
        column_list_ = repr(DAOClass(dto)).split(",")
        data_frame.columns = column_list_
        return data_frame

    @staticmethod
    def set_dto_data_frame(dto, data_frame=None):
        if data_frame is None:
            return None
        column_list_ = repr(dto()).split(",")
        print(column_list_)
        data_frame.columns = column_list_
        return data_frame
