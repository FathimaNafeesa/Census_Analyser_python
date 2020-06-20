from dao_class_census_analyser import *


class CensusAdapter:

    def get_dao_data_frame(self, obj, data_frame=None):
        self.obj = obj
        if data_frame is None:
            return None
        column_list_ = repr(DAOClass()).split(",")
        data_frame.columns = column_list_
        return data_frame
