import matplotlib.pyplot as plt
import utils, tools
from core import selections

def draw_T(dataset, DCT, ID):
    cnt_files = 0
    for data in dataset:
        T = utils.T(data, DCT[cnt_files])
        WL = data["WL"]
        plt.plot(WL, T, "o", label="Filter ID: " + ID[cnt_files])
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Transmittance %")
        plt.grid("on")
        plt.legend(loc="best")
        cnt_files += 1