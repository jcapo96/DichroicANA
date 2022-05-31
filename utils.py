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

