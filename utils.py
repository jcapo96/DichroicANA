import pandas as pd
import numpy as np
import os, glob

def get_path_to_data(row):
    path= os.path.dirname(os.path.dirname(os.getcwd()))
    text_files = glob.glob(path + "/**/" + row["Filename"] + ".txt", recursive = True)
    path_to_file = text_files[0]
    names = ["WL", "TF", "TNF", "RF"]
    data = pd.DataFrame(pd.read_csv(str(path_to_file), sep='\t', skiprows=1, names=names))
    return data

def T(dataset, DCT):
    T = (dataset["TF"]-DCT)/(dataset["TNF"]-DCT)
    return T*100

def QE(PMT):
    path= os.path.dirname(os.path.dirname(os.getcwd()))
    text_files = glob.glob(path + "/**/" + str(PMT) + ".txt", recursive = True)
    path_to_file = text_files[0]
    names = ["WL", "QE"]
    data = pd.DataFrame(pd.read_csv(str(path_to_file), sep='\t', header=0, names=names))
    return data

def R(dataset, PMT_T, PMT_R, DCT, DCR):
    QE_T = QE(PMT_T).loc[QE(PMT_T)["WL"].isin(QE(PMT_R)["WL"])].reset_index(drop=True)
    QE_T = QE_T.loc[QE_T["WL"].isin(dataset["WL"])].reset_index(drop=True)
    QE_R = QE(PMT_R).loc[QE(PMT_R)["WL"].isin(dataset["WL"])].reset_index(drop=True)
    dataset = dataset.loc[dataset["WL"].isin(QE_R["WL"])].reset_index(drop=True)
    QE_R = QE(PMT_R).loc[QE(PMT_R)["WL"].isin(dataset["WL"])].reset_index(drop=True)
    IF_T = (dataset["TF"]-DCT)/QE_T["QE"]
    INF_T = (dataset["TNF"]-DCT)/QE_T["QE"]
    IF_R = (dataset["RF"]-DCR)/QE_R["QE"]
    R = 100*(IF_R/INF_T)
    T = 100*(IF_T/INF_T)
    A = 100-(R + T)
    return (R/np.max(R))*100, dataset["WL"], A, T, IF_T, INF_T, IF_R



