import utils
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

def process_ciemat(filename):
    path= os.path.dirname(os.path.dirname(os.getcwd()))
    text_files = glob.glob(path + "/**/" + filename + ".csv", recursive = True)
    path_to_file = text_files[0]
    desired=[0, 1]
    with open(path_to_file, 'r') as fin:
        reader=csv.reader(fin)
        header=[[str(s) for s in row] for i,row in enumerate(reader) if i in desired]
        config = header[0]
        config = list(filter(None, config))
        header = header[1]
    conf = []
    for i in config:
        conf.append(i[-5:])
    conf.insert(0, "WL")
    cnt = 0
    for i in range(len(header)):
        header[i] = header[i] + str(i)
    data = pd.read_csv(path_to_file, skiprows=2)
    data = data.T.drop_duplicates().T
    data = data.dropna(axis=1)
    data.columns = conf
    print(data.columns)
    return data