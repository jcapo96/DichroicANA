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

def draw_QE(PMT_T, PMT_R):
    QE_T = utils.QE(PMT_T)
    QE_R = utils.QE(PMT_R)
    plt.plot(QE_T["WL"], QE_T["QE"], label=PMT_T)
    plt.plot(QE_R["WL"], QE_R["QE"], label=PMT_R)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("QE %")

def draw_R(dataset, PMT_T, PMT_R, DCT, DCR, ID):
    for data in dataset:
        R = utils.R(data, PMT_T, PMT_R, DCT, DCR)
        plt.plot(R[1], R[0], label=ID)
        plt.xlabel("Wavelenegth (nm)")
        plt.ylabel("Reflectance %")
        plt.legend()

def draw_A(dataset, PMT_T, PMT_R, DCT, DCR, ID):
    for data in dataset:
        R = utils.R(data, PMT_T, PMT_R, DCT, DCR)
        plt.plot(R[1], R[2], label=ID)
        plt.xlabel("Wavelenegth (nm)")
        plt.ylabel("Absorbance %")
        plt.legend()

def draw_ciemat(dataset, angle):
    angle = str(angle)
    for data in dataset:
        plt.plot(data["WL"], data[angle], label="CIEMAT " + angle + " º")
        plt.legend()