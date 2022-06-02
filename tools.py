import utils, utils_ciemat
from core import selections

import os, glob, csv
import pandas as pd
import matplotlib.pyplot as pyplot

def process_data(filters):
    selection = selections.select_files(**filters)
    cnt_files = 0
    filenames = [None]*len(selection)
    angles = [None]*len(selection)
    ID = [None]*len(selection)
    data_files = [None]*len(selection)
    T_files = [None]*len(selection)
    DC_T = [None]*len(selection)
    DC_R = [None]*len(selection)
    PMT_T = [None]*len(selection)
    PMT_R = [None]*len(selection)
    cnt_files = 0
    for index, row in selection.iterrows():
        data = utils.get_path_to_data(row)
        data_files[cnt_files]=data
        T_files[cnt_files] = utils.T(data, float(row["DCT"]))
        DC_T[cnt_files]=float(row["DCT"])
        DC_R[cnt_files]=float(row["DCR"])
        filenames[cnt_files]=row["Filename"]
        angles[cnt_files]=row["Angle"]
        ID[cnt_files]=row["FilterID"]
        PMT_T = row["TReadout"]
        PMT_R = row["RReadout"]
        cnt_files += 1
    return filenames, angles, ID, data_files, T_files, DC_T, DC_R, PMT_T, PMT_R

def process_ciemat(filters):
    selection = selections.select_files(**filters)
    cnt_files = 0
    filenames = [None]*len(selection)
    data_files = [None]*len(selection)
    cnt_files = 0
    for index, row in selection.iterrows():
        data = utils_ciemat.get_path_to_data(row)
        filenames[cnt_files]=row["Filename"]
        data_files[cnt_files]=data
        cnt_files += 1
    return filenames, data_files