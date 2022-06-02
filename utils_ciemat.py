import glob, os, csv
import pandas as pd

def get_path_to_data(row):
    path= os.path.dirname(os.path.dirname(os.getcwd()))
    text_files = glob.glob(path + "/**/" + row["Filename"] + ".csv", recursive = True)
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
    return data