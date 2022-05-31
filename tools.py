import utils
from core import selections
import matplotlib.pyplot as pyplot

def process_data(filters):
    selection = selections.select_files(**filters)
    cnt_files = 0
    filenames = [None]*len(selection)
    ID = [None]*len(selection)
    data_files = [None]*len(selection)
    T_files = [None]*len(selection)
    DC_T = [None]*len(selection)
    DC_R = [None]*len(selection)
    cnt_files = 0
    for index, row in selection.iterrows():
        data = utils.get_path_to_data(row)
        data_files[cnt_files]=data
        T_files[cnt_files] = utils.T(data, float(row["DCT"]))
        DC_T[cnt_files]=float(row["DCT"])
        DC_R[cnt_files]=float(row["DCR"])
        filenames[cnt_files]=row["Filename"]
        ID[cnt_files]=row["FilterID"]
        cnt_files += 1
    return filenames, ID, data_files, T_files, DC_T, DC_R