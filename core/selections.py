import pandas as pd
import numpy as np
import os, glob
import csv

def select_files(**kwargs):
    path_parent = os.path.dirname(os.path.dirname(os.getcwd()))
    cal_logfile = "DichroicLogFile - LogFile.csv"
    destination = glob.glob(path_parent + "/**/**/**/" + cal_logfile , recursive = True)[0]
    #destination = "/home/jordi/Documentos/IFIC-DUNE/Temp-Calibration/CalibrationSystem-jordi/DAQ/Data/RTD_CAL_2022-LogFile - Sheet1.csv"
    # destination =   'C:\\Users\\Usuario\\Documents\\CalibrationSystem\\DAQ\\Data\\RTD_CAL_2022-LogFile - Sheet1.csv'
    #This first part loads the log_file and reads the header, associating each name to the specific column of the log_file_dataframe
    desired=[0]
    with open(destination, 'r') as fin:
        reader=csv.reader(fin)
        header=[[str(s) for s in row] for i,row in enumerate(reader) if i in desired]
        header = header[0]
    for i, j in kwargs.items():
        log_file = pd.DataFrame(pd.read_csv(destination, sep=',', skiprows=1, header=None, names=header))
    
    for i, j in kwargs.items():
        log_file = log_file.loc[(log_file[i]==j)]
    return log_file